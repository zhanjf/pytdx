"""Test the maintained PyTDX handshake and explicit empty/stub responses."""
import unittest
from unittest.mock import Mock,patch
from pytdx.hq import TdxHq_API
from pytdx.parser.get_security_bars import GetSecurityBarsCmd


class PytdxProtocolTests(unittest.TestCase):
    def test_handshake_only_uses_first_two_commands(self):
        api=TdxHq_API();api.client=Mock()
        calls=[]
        with patch('pytdx.hq.SetupCmd1') as first,patch('pytdx.hq.SetupCmd2') as second, \
             patch('pytdx.parser.setup_commands.SetupCmd3') as third:
            first.return_value.call_api.side_effect=lambda:calls.append(1)
            second.return_value.call_api.side_effect=lambda:calls.append(2)
            api.setup();api.setup()
        self.assertEqual(calls,[1,2,1,2]);third.assert_not_called()
        first.assert_called_with(api.client);second.assert_called_with(api.client)

    def test_empty_bar_response_is_valid(self):
        self.assertEqual(GetSecurityBarsCmd(None).parseResponse(b'\x00\x00'),[])

    def test_nonempty_stub_is_explicit_error(self):
        with self.assertRaisesRegex(ValueError,'no actual bars'):
            GetSecurityBarsCmd(None).parseResponse(bytes.fromhex('2003'))

    def test_missing_header_is_explicit_error(self):
        with self.assertRaisesRegex(ValueError,'record-count header'):
            GetSecurityBarsCmd(None).parseResponse(b'')


if __name__=='__main__':unittest.main()
