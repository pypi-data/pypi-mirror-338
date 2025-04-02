# copyright 2004-2023 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact https://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of yams.
#
# yams is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# yams is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with yams. If not, see <https://www.gnu.org/licenses/>.

from logilab.common.testlib import mock_object

import unittest
import warnings

from yams.constraints import (
    Attribute,
    BoundaryConstraint,
    convert_date,
    convert_datetime,
    convert_tzdatetime,
    FormatConstraint,
    IntervalBoundConstraint,
    NOW,
    RegexpConstraint,
    SizeConstraint,
    StaticVocabularyConstraint,
    TODAY,
    UniqueConstraint,
    _check_no_error_during_convert,
    ConstraintJSONEncoder,
)
from yams._exceptions import BadSchemaDefinition
from datetime import datetime, date, time, timedelta, timezone
from dateutil.tz import tzoffset


class CheckAndConverttTC(unittest.TestCase):
    def test_check_no_error_during_convert(self):
        self.assertTrue(_check_no_error_during_convert("4", int))
        self.assertFalse(_check_no_error_during_convert("not a int", int))

    def test_convert_date(self):
        expected = date(1990, 10, 30)
        dt = datetime(1990, 10, 30, 10)
        self.assertEqual(convert_date(expected), expected)
        self.assertEqual(convert_date("1990-10-30"), expected)
        self.assertEqual(convert_date(dt), expected)

        with self.assertRaises(ValueError):
            convert_date("not a date")

    def test_convert_datetime(self):
        expected = datetime(1990, 10, 30, 10)
        self.assertEqual(convert_datetime(expected), expected)
        self.assertEqual(convert_datetime("1990-10-30 10"), expected)

        example_date = date(1990, 10, 30)
        self.assertEqual(convert_datetime(example_date), datetime(1990, 10, 30))

        with self.assertRaises(ValueError):
            convert_datetime("not a datetime")

    def test_convert_tzdatetime_accepts_iso_string(self):
        central_european_time = tzoffset("CET", 3600)  # UTC+01
        expected = datetime(1990, 10, 30, 10, tzinfo=central_european_time)
        self.assertEqual(convert_tzdatetime("1990-10-30T10:00+01"), expected)

    def test_convert_tzdatetime_parses_iso_string_without_tz_as_utc(self):
        expected = datetime(1990, 10, 30, 9, tzinfo=timezone.utc)
        with warnings.catch_warnings(record=True) as w:
            self.assertEqual(convert_tzdatetime("1990-10-30T09:00"), expected)
        self.assertNotEqual([], w)
        self.assertIn("Passing a datetime without timezone is deprecated", str(w[0]))


class ConstraintTC(unittest.TestCase):
    if not hasattr(unittest.TestCase, "subTest"):
        from contextlib import contextmanager

        @contextmanager
        def subTest(self, **kwargs):
            yield

    def test_membership(self):
        s = set()
        cstrs = [
            UniqueConstraint(),
            SizeConstraint(min=0, max=42),
            RegexpConstraint("babar", 0),
            BoundaryConstraint(">", 1),
            IntervalBoundConstraint(minvalue=0, maxvalue=42),
            StaticVocabularyConstraint((1, 2, 3)),
            FormatConstraint(),
        ]
        for cstr in cstrs:
            s.add(cstr)
            s.add(type(cstr).deserialize(cstr.serialize()))
        self.assertEqual(7, len(s))

    def test_interval_serialization_integers(self):
        cstr = IntervalBoundConstraint(minvalue=12, maxvalue=13)
        self.assertEqual(IntervalBoundConstraint.deserialize("12;13"), cstr)
        self.assertEqual(cstr.serialize(), '{"maxvalue": 13, "minvalue": 12, "msg": null}')
        self.assertEqual(cstr.__class__.deserialize(cstr.serialize()), cstr)
        cstr = IntervalBoundConstraint(maxvalue=13)
        self.assertEqual(IntervalBoundConstraint.deserialize("None;13"), cstr)
        self.assertEqual(cstr.serialize(), '{"maxvalue": 13, "minvalue": null, "msg": null}')
        self.assertEqual(cstr.__class__.deserialize(cstr.serialize()), cstr)
        cstr = IntervalBoundConstraint(minvalue=13)
        self.assertEqual(IntervalBoundConstraint.deserialize("13;None"), cstr)
        self.assertEqual(cstr.serialize(), '{"maxvalue": null, "minvalue": 13, "msg": null}')
        self.assertEqual(cstr.__class__.deserialize(cstr.serialize()), cstr)
        self.assertRaises(AssertionError, IntervalBoundConstraint)

    def test_interval_serialization_floats(self):
        cstr = IntervalBoundConstraint(minvalue=12.13, maxvalue=13.14)
        self.assertEqual(IntervalBoundConstraint.deserialize("12.13;13.14"), cstr)
        self.assertEqual(cstr.serialize(), '{"maxvalue": 13.14, "minvalue": 12.13, "msg": null}')
        self.assertEqual(cstr.__class__.deserialize(cstr.serialize()), cstr)

    def test_interval_deserialization_integers(self):
        cstr = IntervalBoundConstraint.deserialize("12;13")
        self.assertEqual(cstr.minvalue, 12)
        self.assertEqual(cstr.maxvalue, 13)
        cstr = IntervalBoundConstraint.deserialize("None;13")
        self.assertEqual(cstr.minvalue, None)
        self.assertEqual(cstr.maxvalue, 13)
        cstr = IntervalBoundConstraint.deserialize("12;None")
        self.assertEqual(cstr.minvalue, 12)
        self.assertEqual(cstr.maxvalue, None)

    def test_interval_deserialization_floats(self):
        cstr = IntervalBoundConstraint.deserialize("12.13;13.14")
        self.assertEqual(cstr.minvalue, 12.13)
        self.assertEqual(cstr.maxvalue, 13.14)

    def test_interval_attribute_error(self):
        cstr = IntervalBoundConstraint(minvalue=Attribute("hip"), maxvalue=Attribute("hop"))

        class entity:
            hip, hop = 34, 42

        self.assertEqual(
            cstr.failed_message("key", 20, entity),
            (
                "value %(KEY-value)s must be >= %(KEY-boundary)s",
                {"key-boundary": "hip", "key-value": 20},
            ),
        )
        self.assertEqual(
            cstr.failed_message("key", 43, entity),
            (
                "value %(KEY-value)s must be <= %(KEY-boundary)s",
                {"key-boundary": "hop", "key-value": 43},
            ),
        )

    def test_regexp_serialization(self):
        cstr = RegexpConstraint("[a-z]+,[A-Z]+", 40)
        self.assertEqual(cstr.serialize(), '{"flags": 40, "msg": null, "regexp": "[a-z]+,[A-Z]+"}')
        self.assertEqual(cstr.__class__.deserialize(cstr.serialize()), cstr)

    def test_regexp_deserialization(self):
        cstr = RegexpConstraint.deserialize("[a-z]+,[A-Z]+,40")
        self.assertEqual(cstr.regexp, "[a-z]+,[A-Z]+")
        self.assertEqual(cstr.flags, 40)

    def test_interval_with_attribute(self):
        cstr = IntervalBoundConstraint(minvalue=NOW(type="Datetime"), maxvalue=Attribute("hop"))
        cstr2 = IntervalBoundConstraint.deserialize(cstr.serialize())
        self.assertEqual(cstr2.minvalue.offset, None)
        self.assertEqual(cstr2.maxvalue.attr, "hop")
        self.assertTrue(
            cstr2.check(
                mock_object(hop=datetime.now() + timedelta(hours=1)),
                "hip",
                datetime.now() + timedelta(seconds=2),
            )
        )
        # fail, value < minvalue
        self.assertFalse(
            cstr2.check(
                mock_object(hop=datetime.now() + timedelta(hours=1)),
                "hip",
                datetime.now() - timedelta(hours=2),
            )
        )
        # fail, value > maxvalue
        self.assertFalse(
            cstr2.check(
                mock_object(hop=datetime.now() + timedelta(hours=1)),
                "hip",
                datetime.now() + timedelta(hours=2),
            )
        )

    def test_interval_with_date(self):
        cstr = IntervalBoundConstraint(minvalue=TODAY(timedelta(1)), maxvalue=TODAY(timedelta(3)))
        cstr2 = IntervalBoundConstraint.deserialize(cstr.serialize())
        self.assertEqual(cstr2.minvalue.offset, timedelta(1))
        self.assertEqual(cstr2.maxvalue.offset, timedelta(3))
        self.assertTrue(cstr2.check(None, "hip", date.today() + timedelta(2)))
        # fail, value < minvalue
        self.assertFalse(cstr2.check(None, "hip", date.today()))
        # fail, value > maxvalue
        self.assertFalse(cstr2.check(None, "hip", date.today() + timedelta(4)))

    def test_boundary_constraint_consistency(self):
        cstr = BoundaryConstraint("<=", NOW(type="TZDatetime"))
        subjschema = mock_object()
        valid_objschema = mock_object(type="TZDatetime", final=True)
        rdef = mock_object()

        # Consistent
        cstr.check_consistency(subjschema, valid_objschema, rdef)

        # BoundaryConstraint doesn't apply to non final attribute schema
        non_final_objschema = mock_object(type="TZDatetime", final=False)
        with self.assertRaisesRegex(BadSchemaDefinition, "non final entity type"):
            cstr.check_consistency(subjschema, non_final_objschema, rdef)

        # BoundaryConstraint with NOW/TODAY as boundary must match type of the attribute schema
        inconsistent_objschema = mock_object(type="Datetime", final=True)
        with self.assertRaisesRegex(BadSchemaDefinition, "got Datetime"):
            cstr.check_consistency(subjschema, inconsistent_objschema, rdef)

    def test_bound_constant(self):
        cstr = BoundaryConstraint("<=", 0)
        cstr2 = BoundaryConstraint.deserialize(cstr.serialize())
        self.assertFalse(cstr2.check(None, "hip", 25))
        self.assertTrue(cstr2.check(None, "hip", -1))

    def test_bound_with_attribute(self):
        cstr = BoundaryConstraint("<=", Attribute("hop"))
        cstr2 = BoundaryConstraint.deserialize(cstr.serialize())
        self.assertEqual(cstr, cstr2)
        self.assertEqual(cstr2.boundary.attr, "hop")
        self.assertEqual(cstr2.operator, "<=")
        self.assertTrue(cstr2.check(mock_object(hop=date.today()), "hip", date.today()))
        # fail, value > maxvalue
        self.assertFalse(
            cstr2.check(mock_object(hop=date.today()), "hip", date.today() + timedelta(days=1))
        )

    def test_bound_with_date(self):
        cstr = BoundaryConstraint("<=", TODAY())
        cstr2 = BoundaryConstraint.deserialize(cstr.serialize())
        self.assertEqual(cstr, cstr2)
        self.assertEqual(cstr2.boundary.offset, None)
        self.assertEqual(cstr2.operator, "<=")
        self.assertTrue(cstr2.check(None, "hip", date.today()))
        # fail, value > maxvalue
        self.assertFalse(cstr2.check(None, "hip", date.today() + timedelta(days=1)))

    def test_bound_with_unset_attribute(self):
        cstr = BoundaryConstraint("<=", None)
        self.assertTrue(cstr.check(None, "hip", date.today()))
        cstr = BoundaryConstraint("<=", Attribute("unset_attr"))
        self.assertTrue(cstr.check(mock_object(unset_attr=None), "hip", date.today()))

    def test_boundary_constraint_message(self):
        cstr = BoundaryConstraint("<=", 0)
        self.assertEqual(
            cstr.failed_message("attr", 1, object()),
            (
                "value %(KEY-value)s must be <= %(KEY-boundary)s",
                {"attr-value": 1, "attr-boundary": 0},
            ),
        )

    def test_vocab_constraint_serialization(self):
        cstr = StaticVocabularyConstraint(["a, b", "c"])
        self.assertEqual(
            StaticVocabularyConstraint.deserialize(cstr.serialize()).values, ("a, b", "c")
        )

    def test_custom_message(self):
        cstrs = [
            UniqueConstraint(msg="constraint failed, you monkey!"),
            SizeConstraint(min=0, max=42, msg="constraint failed, you monkey!"),
            RegexpConstraint("babar", 0, msg="constraint failed, you monkey!"),
            BoundaryConstraint(">", 1, msg="constraint failed, you monkey!"),
            IntervalBoundConstraint(minvalue=0, maxvalue=42, msg="constraint failed, you monkey!"),
            StaticVocabularyConstraint((1, 2, 3), msg="constraint failed, you monkey!"),
            FormatConstraint(msg="constraint failed, you monkey!"),
        ]
        for cstr in cstrs:
            with self.subTest(cstr=cstr):
                self.assertEqual(
                    cstr.failed_message("key", "value", object()),
                    ("constraint failed, you monkey!", {}),
                )
            cstr = type(cstr).deserialize(cstr.serialize())
            with self.subTest(cstr=cstr):
                self.assertEqual(
                    cstr.failed_message("key", "value", object()),
                    ("constraint failed, you monkey!", {}),
                )


class ConstraintJSONEncoderTC(unittest.TestCase):
    encoder = ConstraintJSONEncoder()

    def test_now(self):
        self.assertIn("__now__", self.encoder.default(NOW()))

    def test_today(self):
        self.assertIn("__today__", self.encoder.default(TODAY()))

    def test_date(self):
        self.assertEqual(self.encoder.default(date(2023, 11, 28)), "2023-11-28")

    def test_time(self):
        self.assertEqual(self.encoder.default(time(16, 43)), "16:43:00")

    def test_datetime(self):
        self.assertEqual(
            self.encoder.default(datetime(2023, 11, 28, 16, 43)), "2023-11-28T16:43:00"
        )


if __name__ == "__main__":
    unittest.main()
