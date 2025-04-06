from cacofonisk.callerid import CallerId
from cacofonisk.channel import SimpleChannel
from tests.replaytest import ChannelEventsTestCase


class TestAttnXfer(ChannelEventsTestCase):
    
    def test_xfer_abbc(self):
        """
        Test threeway transfer where B merges with A and C.

        First of all, we need to get notifications that calls are being
        made:
        - 203 (150010003) calls 202 (150010002)
        - 202 calls 204 (150010004)

        Secondly, we need notifications that an threeway transfer has
        happened:
        - 202 joins the channels (202, 204) into a single brigde
        """
        self.maxDiff = None
        events_file = 'fixtures/xfer_threeway/xfer_threeway_abbc.json'
        events = self.run_and_get_events(events_file)

        a_chan = SimpleChannel(
            name='PJSIP/150010003-00000003',
            uniqueid='ac670c3c69a6-1698413067.111',
            linkedid='ac670c3c69a6-1698413067.111',
            account_code='150010003',
            caller_id=CallerId(name='Megan Estes', num='203'),
            cid_calling_pres='1 (Presentation Allowed, Passed Screen)',
            connected_line=CallerId(num="202"),
            exten='202',
            state=6,
        )

        a_chan_3pcc = a_chan.replace(
            name='SIP/150010001-0000002a',
            uniqueid='195176c06ab8-1529941225.617',
            linkedid='195176c06ab8-1529941225.617',
            exten='203',
        )

        b_chan = SimpleChannel(
            name='PJSIP/150010002-00000004',
            uniqueid='ac670c3c69a6-1698413067.122',
            linkedid='ac670c3c69a6-1698413067.111',
            account_code='150010003',
            caller_id=CallerId(num='202'),
            cid_calling_pres='0 (Presentation Allowed, Not Screened)',
            connected_line=CallerId(name='Megan Estes', num='203'),
            exten='s',
            state=6,
        )

        b_chan_transferred = b_chan.replace(exten='203')

        c_chan = SimpleChannel(
            name='SIP/150010003-0000002b',
            uniqueid='195176c06ab8-1529941225.625',
            linkedid='195176c06ab8-1529941225.617',
            account_code='150010001',
            caller_id=CallerId(num='203'),
            cid_calling_pres='0 (Presentation Allowed, Not Screened)',
            connected_line=CallerId(name='Andrew Garza', num='201'),
            exten='s',
            state=6,
        )

        expected_events = [
            ('on_b_dial', {
                'caller': a_chan.replace(state=4),
                'targets': [b_chan.replace(state=5)],
            }),
            ('on_up', {
                'caller': a_chan,
                'target': b_chan,
            }),
            ('on_b_dial', {
                'caller': a_chan.replace(state=4), # ?
                'targets': [c_chan.replace(state=5)],
            }),
            ('on_up', {
                'caller': a_chan_3pcc,
                'target': c_chan,
            }),
            ('on_threeway_transfer', {
                'caller': b_chan_transferred,
                'target': c_chan,
                'transferer': a_chan_3pcc,
            }),
            ('on_hangup', {
                'caller': b_chan_transferred,
                'reason': 'completed',
            }),
            ('on_hangup', {
                'caller': b_chan_transferred,
                'reason': 'completed',
            }),
        ]

        self.assertEqual(expected_events, events)
