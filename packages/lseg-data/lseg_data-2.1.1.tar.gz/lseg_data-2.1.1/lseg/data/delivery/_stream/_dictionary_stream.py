from ._omm_stream import PrvOMMStream


class PrvDictionaryStream(PrvOMMStream):
    @property
    def open_message(self) -> dict:
        msg = {
            "ID": self.id,
            "Type": "Request",
            "Domain": "Dictionary",
            "Key": {"Filter": 7, "Name": self.name, "NameType": "Name"},
            "Streaming": False,
        }

        if self._service is not None:
            msg["Key"]["Service"] = self._service

        return msg
