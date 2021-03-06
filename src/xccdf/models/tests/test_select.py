# -*- coding: utf-8 -*-

# Python stdlib
import unittest
import os
import io
import sys

# lxml
from lxml import etree

# XCCDF
from xccdf.models.select import Select
from xccdf.exceptions import RequiredAttributeException, InvalidValueException


class SelectTestCase(unittest.TestCase):

    """
    Test cases for Title class
    """

    def load_example_element(self, xml_file_type='ok'):
        """
        Helper method to load an XML element
        """

        file_name = 'example_xccdf_select_{type}.xml'.format(
            type=xml_file_type)

        xml_path = os.path.abspath(os.path.dirname(__file__))
        xml_file = io.open(os.path.join(
            xml_path,
            'examples',
            file_name))

        xml_string = xml_file.read()
        xml_file.close()

        element_tree = etree.fromstring(xml_string.encode('utf-8'))

        return element_tree[1][0]

    def create_select_object(self, object_type='ok'):
        """
        Helper method to create the Select object

        :returns: Select object
        :rtype: xccdf.models.select.Select
        """

        xml_element = self.load_example_element(object_type)

        return Select(xml_element)

    def test_init_all_ok(self):
        """
        Tests the class constructor
        """

        xccdf_select = self.create_select_object('ok')

        self.assertEqual(xccdf_select.name, 'select',
                         'select tag name does not match')

        self.assertTrue(hasattr(xccdf_select, 'idref'))

        self.assertTrue(hasattr(xccdf_select, 'selected'))

    def test_init_no_xml_element(self):
        """
        Tests the class constructor from an empty instance
        """

        idref = 'usgcb-rhel5desktop-rule-2.1.1.1.1.a'
        xccdf_select = Select(idref=idref)

        self.assertEqual(xccdf_select.name, 'select',
                         'select tag name does not match')

        self.assertEqual(xccdf_select.idref, idref,
                         'select idref does not match')

        self.assertFalse(xccdf_select.is_selected())

    def test_init_with_empty_instance(self):
        """
        Tests the class constructor from an empty instance
        """

        error_msg = 'either xml_element or idref are required'

        if sys.version_info[0] >= 3 and sys.version_info[1] >= 2:
            with self.assertRaisesRegex(ValueError,
                                        error_msg):
                Select()
        else:
            with self.assertRaisesRegexp(ValueError,
                                         error_msg):
                Select()

    def test_init_no_xml_element_selected(self):
        """
        Tests the class constructor from an empty instance with selected true
        """

        idref = 'usgcb-rhel5desktop-rule-2.1.1.1.1.a'
        xccdf_select = Select(idref=idref, selected=True)

        self.assertEqual(xccdf_select.name, 'select',
                         'select tag name does not match')

        self.assertEqual(xccdf_select.idref, idref,
                         'select idref does not match')

        self.assertTrue(xccdf_select.is_selected())

    def test_init_no_idref(self):
        """
        Tests the class constructor without an id
        """

        error_msg = 'idref attribute required'

        if sys.version_info[0] >= 3 and sys.version_info[1] >= 2:
            with self.assertRaisesRegex(RequiredAttributeException,
                                        error_msg):
                self.create_select_object('no_idref')
        else:
            with self.assertRaisesRegexp(RequiredAttributeException,
                                         error_msg):
                self.create_select_object('no_idref')

    def test_init_invalid_selected(self):
        """
        Tests the class constructor with an invalid selected value
        """

        error_msg = 'selected attribute has a invalid value'

        if sys.version_info[0] >= 3 and sys.version_info[1] >= 2:
            with self.assertRaisesRegex(InvalidValueException,
                                        error_msg):
                self.create_select_object('invalid_selected')
        else:
            with self.assertRaisesRegexp(InvalidValueException,
                                         error_msg):
                self.create_select_object('invalid_selected')

    def test_print_object(self):
        """
        Tests the string representation of an Select object
        """

        xccdf_select = self.create_select_object('ok')

        string_value = 'select {idref} {sel}'.format(
            idref=xccdf_select.idref, sel=str(xccdf_select.is_selected()))
        self.assertEqual(str(xccdf_select), string_value,
                         'String representation does not match')

    def test_print_object_empty_instance(self):
        """
        Tests the string representation of an Select object
        from an empty instance
        """

        idref = 'usgcb-rhel5desktop-rule-2.1.1.1.1.a'
        xccdf_select = Select(idref=idref)

        string_value = 'select {idref} {sel}'.format(idref=idref, sel=False)
        self.assertEqual(str(xccdf_select), string_value,
                         'String representation does not match')

    def test_method_is_selected_true(self):
        """
        Tests the is_selected method returning true
        """

        xccdf_select = self.create_select_object('ok')

        self.assertTrue(xccdf_select.is_selected(),
                        'Expected True in selected')

    def test_method_is_selected_false(self):
        """
        Tests the is_selected method returning false
        """

        xccdf_select = self.create_select_object('false')

        self.assertFalse(xccdf_select.is_selected(),
                         'Expected False in selected')

    def test_method_update_xml_element(self):
        """
        Tests the update_xml_element method
        """

        xccdf_select = self.create_select_object('ok')

        new_idref = 'test_id_ref'

        self.assertNotEqual(xccdf_select.idref, new_idref,
                            'New idref is equal to original')

        xccdf_select.idref = new_idref
        xccdf_select.update_xml_element()

        self.assertEqual(xccdf_select.xml_element.attrib['idref'], new_idref,
                         'XML idref does not match new idref')
        self.assertEqual(xccdf_select.idref, new_idref,
                         'Title idref does not match new idref')

    def test_method_update_xml_element_empty_instance(self):
        """
        Tests the update_xml_element method with an empty instance
        """

        idref = 'usgcb-rhel5desktop-rule-2.1.1.1.1.a'
        xccdf_select = Select(idref=idref)

        self.assertFalse(hasattr(xccdf_select, 'xml_element'),
                         'XML element is defined')

        xccdf_select.update_xml_element()

        self.assertTrue(hasattr(xccdf_select, 'xml_element'),
                        'XML element is not defined')

    def test_method_to_xml_string(self):
        """
        Tests the to_xml_string method
        """

        xccdf_select = self.create_select_object('ok')

        xml_content = xccdf_select.to_xml_string()

        new_xccdf_select = Select(
            etree.fromstring(xml_content.encode('utf-8')))

        self.assertEqual(xccdf_select.idref, new_xccdf_select.idref,
                         'Select idref does not match')
        self.assertEqual(xccdf_select.selected, new_xccdf_select.selected,
                         'Select selected does not match')


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(SelectTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
