"""Module to handle XML input and output"""

import os
import sys
from lxml import etree
import lvlspy.level as lv
import lvlspy.species as ls
import lvlspy.transition as lt


def write_to_xml(coll, file, pretty_print=True, units="keV"):
    """Method to write the collection to XML.

    Args:
        ``coll`` (:obj: `obj') The collection to be written to the XML file
        ``file`` (:obj:`str`) The output file name.

        ``pretty_print`` (:obj:`bool`, optional): If set to True,
        routine outputs the xml in nice indented format.

        ``units`` (:obj:`str`, optional): A string for the energy units.

    Return:
        On successful return, the species collection data have been
        written to the XML output file.

    """

    root = etree.Element("species_collection")
    xml = etree.ElementTree(root)

    _add_optional_properties(root, coll)

    for species_name, species in coll.get().items():
        my_species = etree.SubElement(root, "species", name=species_name)

        _add_optional_properties(my_species, species)

        xml_levels = etree.SubElement(my_species, "levels")

        for level in species.get_levels():
            _add_level_to_xml(xml_levels, species, level, units)

    xml.write(file, pretty_print=pretty_print)


def _add_level_to_xml(xml_levels, species, level, units):
    result = etree.SubElement(xml_levels, "level")
    _add_optional_properties(result, level)
    result_props = etree.SubElement(result, "properties")
    if units != "keV":
        my_energy = etree.SubElement(result_props, "energy", units=units)
    else:
        my_energy = etree.SubElement(result_props, "energy")
    my_energy.text = _get_energy_text(level.get_energy(), units)
    my_multiplicity = etree.SubElement(result_props, "multiplicity")
    my_multiplicity.text = str(level.get_multiplicity())

    _add_transitions_to_xml(result, species, level, units)

    return result


def _add_transitions_to_xml(xml_level, species, level, units):
    lower_levels = species.get_lower_linked_levels(level)

    if len(lower_levels) == 0:
        return

    xml_transitions = etree.SubElement(xml_level, "transitions")

    for lower_level in lower_levels:
        transition = species.get_level_to_level_transition(level, lower_level)
        xml_trans = etree.SubElement(xml_transitions, "transition")
        _add_optional_properties(xml_trans, transition)
        if units != "keV":
            xml_to_energy = etree.SubElement(
                xml_trans, "to_energy", units=units
            )
        else:
            xml_to_energy = etree.SubElement(xml_trans, "to_energy")
        xml_to_energy.text = _get_energy_text(lower_level.get_energy(), units)
        xml_to_multiplicity = etree.SubElement(xml_trans, "to_multiplicity")
        xml_to_multiplicity.text = str(lower_level.get_multiplicity())
        xml_a = etree.SubElement(xml_trans, "a")
        xml_a.text = str(transition.get_einstein_a())


def _add_optional_properties(my_element, my_object):
    my_props = my_object.get_properties()

    if len(my_props):
        props = etree.SubElement(my_element, "optional_properties")
        for prop in my_props:
            if isinstance(prop, str):
                my_prop = etree.SubElement(props, "property", name=prop)
            elif isinstance(prop, tuple):
                if len(prop) == 2:
                    my_prop = etree.SubElement(
                        props, "property", name=prop[0], tag1=prop[1]
                    )
                elif len(prop) == 3:
                    my_prop = etree.SubElement(
                        props,
                        "property",
                        name=prop[0],
                        tag1=prop[1],
                        tag2=prop[2],
                    )
            else:
                print("Improper property key")
                sys.exit()

            my_prop.text = str(my_props[prop])


def validate(file):
    """Method to validate a species collection XML file.

    Args:
        ``file`` (:obj:`str`) The name of the XML file to validate.

    Returns:
        An error message if invalid and nothing if valid.

    """

    parser = etree.XMLParser(remove_blank_text=True)
    xml = etree.parse(file, parser)
    xml.xinclude()

    schema_file = os.path.join(os.path.dirname(__file__), "xsd_pub/spcoll.xsd")
    xmlschema_doc = etree.parse(schema_file)

    xml_validator = etree.XMLSchema(xmlschema_doc)
    xml_validator.validate(xml)


def update_from_xml(coll, file, xpath=""):
    """Method to update a species collection from an XML file.

    Args:
        ``coll`` (:obj:`obj`) The collection to be read from the XML file

        ``file`` (:obj:`str`) The name of the XML file from which to update.

        ``xpath`` (:obj:`str`, optional): XPath expression to select
        species.  Defaults to all species.

    Returns:
        On successful return, the species collection has been updated.

    """

    parser = etree.XMLParser(remove_blank_text=True)
    xml = etree.parse(file, parser)
    xml.xinclude()

    spcoll = xml.getroot()

    _update_optional_properties(spcoll, coll)

    for xml_species in spcoll.xpath("//species" + xpath):
        coll.add_species(_get_species_from_xml(xml_species))


def _get_species_from_xml(xml_species):
    level_dict = {}
    result = ls.Species(xml_species.attrib["name"])
    _update_optional_properties(xml_species, result)
    for xml_level in xml_species.xpath(".//level"):
        new_level = _get_level_from_xml(xml_level)
        result.add_level(new_level)
        level_dict[new_level.get_energy()] = new_level

        for xml_trans in xml_level.xpath(".//transition"):
            trans = _get_transition_from_xml(xml_trans, new_level, level_dict)
            if trans:
                result.add_transition(trans)

    return result


def _get_level_from_xml(xml_level):
    props = xml_level.xpath(".//properties")
    energy = props[0].xpath(".//energy")
    multiplicity = props[0].xpath(".//multiplicity")
    attributes = energy[0].attrib
    if "units" in attributes:
        result = lv.Level(
            float(energy[0].text),
            int(multiplicity[0].text),
            units=attributes["units"],
        )
    else:
        result = lv.Level(float(energy[0].text), int(multiplicity[0].text))
    _update_optional_properties(xml_level, result)

    return result


def _get_transition_from_xml(xml_trans, upper_level, level_dict):
    to_energy = xml_trans.xpath(".//to_energy")
    to_a = xml_trans.xpath(".//a")

    f_to_energy = _convert_to_kev(to_energy)
    if f_to_energy in level_dict:
        result = lt.Transition(
            upper_level,
            level_dict[f_to_energy],
            float(to_a[0].text),
        )
        _update_optional_properties(xml_trans, result)
        return result
    return None


def _convert_to_kev(energy):
    attributes = energy[0].attrib
    result = float(energy[0].text)
    if "units" in attributes:
        result /= lv.units_dict[attributes["units"]]
    return result


def _get_energy_text(energy, units):
    return str(energy * lv.units_dict[units])


def _update_optional_properties(my_element, my_object):
    opt_props = my_element.xpath("optional_properties")

    if len(opt_props) > 0:
        props = opt_props[0].xpath("property")

        my_props = {}
        for prop in props:
            attributes = prop.attrib
            my_keys = attributes.keys()
            if len(my_keys) == 1:
                my_props[attributes[my_keys[0]]] = prop.text
            elif len(my_keys) == 2:
                my_props[(attributes[my_keys[0]], attributes[my_keys[1]])] = (
                    prop.text
                )
            elif len(my_keys) == 3:
                my_props[
                    (
                        attributes[my_keys[0]],
                        attributes[my_keys[1]],
                        attributes[my_keys[2]],
                    )
                ] = prop.text
            else:
                print("Improper keys for property")
                sys.exit()

        my_object.update_properties(my_props)
