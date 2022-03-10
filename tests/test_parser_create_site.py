import unittest
from tabcmd.parsers.create_site_parser import CreateSiteParser
from .common_setup import *

commandname = "createsite"


class CreateSiteParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser_under_test, manager, mock_command = initialize_test_pieces(commandname)
        CreateSiteParser.create_site_parser(manager, mock_command)

    def test_create_site_parser_just_a_name(self):
        mock_args = [commandname, "site-name"]
        args = self.parser_under_test.parse_args(mock_args)
        assert args.site_name == "site-name", args

    def test_create_site_parser_missing_required_name(self):
        mock_args = [commandname]
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(mock_args)

    def test_create_site_parser_user_quota_integer(self):
        mock_args = [commandname, "site-name", "--user-quota"]
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(mock_args)

    def test_create_site_parser_with_all_args(self):
        mock_args = [
            commandname,
            "site-name",
            "--user-quota",
            "12",
            "--storage-quota",
            "12",
        ]  # what else?
        args = self.parser_under_test.parse_args(mock_args)
        print(args)
        assert args.site_name == "site-name", args
        assert args.user_quota == 12, args
        assert args.storage_quota == 12, args
