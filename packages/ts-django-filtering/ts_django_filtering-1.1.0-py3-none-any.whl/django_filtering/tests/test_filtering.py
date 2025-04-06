from django.test import TestCase

from .. import FilterSet, Filter
from ..models import Requirement, Job, Person


class TestFiltering(TestCase):
    def setUp(self):
        self.requirements = Requirement.objects.bulk_create([
            Requirement(
                details=f"REQ{i}"
            ) for i in range(0, 3)
        ])

        self.jobs = Job.objects.bulk_create([
            Job(
                name=f"JOB{i}",
                value=i,
                requirement=self.requirements[i],
            ) for i in range(0, 3)
        ])

        self.people = Person.objects.bulk_create([
            Person(
                name=name,
                value=idx,
                job=self.jobs[idx]
            ) for idx, name in enumerate(["Joe Mama", "Ben Bunger", "Larry"])
        ])

    def test_filtering(self):
        filter_1 = Filter(
            path="name",
            operator="exact",
            value="Joe Mama"
        )
        filter_2 = Filter(
            path="job.name",
            operator="exact",
            value="JOB1"
        )
        filter_3 = Filter(
            path="job.requirement.details",
            operator="exact",
            value="REQ2"
        )
        filter_4 = Filter(
            path="name",
            operator="contains",
            value="TEST BAD DATA",
        )
        filter_5 = Filter(
            path="job.value",
            operator="gte",
            value="1",
        )

        a = FilterSet(filters=[filter_1]).filter(Person)
        b = FilterSet(filters=[filter_2]).filter(Person)
        c = FilterSet(filters=[filter_3]).filter(Person)
        d = FilterSet(filters=[filter_4]).filter(Person)
        e = FilterSet(filters=[filter_5]).filter(Person)

        self.assertQuerySetEqual(a, [Person.objects.get(pk=1)])
        self.assertQuerySetEqual(b, [Person.objects.get(pk=2)])
        self.assertQuerySetEqual(c, [Person.objects.get(pk=3)])
        self.assertQuerySetEqual(d, [])
        self.assertQuerySetEqual(list(e), [Person.objects.get(pk=2), Person.objects.get(pk=3)])

    def test_instance_filtering(self):
        people = list(Person.objects.all())

        a = FilterSet(filters=[
            Filter(
                path="name",
                operator="exact",
                value="Joe Mama"
            )
        ]).filter(people)

        b = FilterSet(filters=[
            Filter(
                path="job.name",
                operator="in",
                value=[
                    "JOB1",
                    "JOB2",
                ]
            )
        ]).filter(people)

        c = FilterSet(filters=[
            Filter(
                path="job.requirement.details",
                operator="regex",
                value=r"^REQ(?:1|2)$"
            )
        ]).filter(people)

        d = FilterSet(filters=[
            Filter(
                path="name",
                operator="istartswith",
                value="lar"
            )
        ]).filter(people)

        e = FilterSet(filters=[
            Filter(
                path="name",
                operator="endswith",
                value="ry"
            )
        ]).filter(people)

        f = FilterSet(filters=[
            Filter(
                path="name",
                operator="isnotnull",
                value=None
            )
        ]).filter(people)

        g = FilterSet(filters=[
            Filter(
                path="name",
                operator="isnull",
                value=None
            )
        ]).filter(people)

        self.assertEqual(len(a), 1)
        self.assertEqual(a[0], self.people[0])

        self.assertEqual(len(b), 2)
        self.assertEqual(b[0], self.people[1])
        self.assertEqual(b[1], self.people[2])

        self.assertEqual(len(c), 2)
        self.assertEqual(c[0], self.people[1])
        self.assertEqual(c[1], self.people[2])

        self.assertEqual(len(d), 1)
        self.assertEqual(d[0], self.people[2])
        self.assertEqual(e[0], d[0])

        self.assertEqual(len(f), 3)
        self.assertEqual(len(g), 0)
