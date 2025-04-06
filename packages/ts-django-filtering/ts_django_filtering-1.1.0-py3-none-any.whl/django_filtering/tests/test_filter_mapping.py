import operator

from django.test import TestCase

from django_filtering.filter import Filter, CustomOperators


class TestFilterMapping(TestCase):
    def test_json(self):
        this_filter = Filter(
            path="a.b.c",
            operator="lt",
            value="test"
        )

        self.assertDictEqual(this_filter.json, {"a__b__c__lt": "test"})

    def test_invalid_operator(self):
        self.assertRaises(
            ValueError,
            Filter,
            path="a",
            operator="invalid operator test",  # noqa
            value="test",
        )

    def test_mapped_operator(self):
        lt = Filter(
            path="a",
            operator="lt",
            value=1
        )

        regex = Filter(
            path="a",
            operator="regex",
            value=r"^test$",
        )

        self.assertEqual(lt.mapped_operator, operator.lt)
        self.assertEqual(regex.mapped_operator, CustomOperators.regex)

    def test_merge_to_dict(self):
        filters = [
            Filter(
                path=f"test.{i}",
                operator="exact",
                value="test",
            ) for i in range(0, 5)
        ]

        json_filters = {'test__0__exact': 'test', 'test__1__exact': 'test', 'test__2__exact': 'test', 'test__3__exact': 'test', 'test__4__exact': 'test'}

        self.assertDictEqual(json_filters, Filter.merge_to_dict(*filters))
