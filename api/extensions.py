from types import SimpleNamespace
from typing import Optional
from urllib import response
from .request import request
from .utils import make_payload
from . import constants

class Extensions(request):
    extensions_list = {}

    def __init__(self) -> None:
        super().__init__()

    def get_extensions(self, **kwargs) -> dict:
        """
        Get all extensions
        """
        self.extensions_list = self.get('ExtensionList', **kwargs).json().get('list')
        return self.extensions_list
    
    def get_extension(self, extension_id, **kwargs) -> dict:
        """
        Get an extension
        """
        for ext in self.extensions_list:
            if ext.get('id') == extension_id:
                self.extension = ext
                break
            if kwargs:
                for k, v in kwargs.items():
                    if ext.get(k) == v:
                        self.extension = ext
                        break
        return self.extension

    def get_qrcode(self, extension_id, **kwargs) -> dict:
        """
        Get an extension qrcode
        """
        response = self.get(f"ExtensionList")
        data = response.json().get('list')
        self.extension_id = int("".join([str(i['Id']) for i in data if i['Number'] == str(extension_id)]))
        if self.extension_id:
            response = self.post('ExtensionList/set',{'Id': self.extension_id}).json()
            qrcode = constants.BASEURL.format(self.fqdn, self.port+response['ActiveObject']['MyPhoneProvLink']['_value'])
            return qrcode
        # 
        # pass
    def set_extension(self, extension_id, **kwargs) -> dict:
        """
        Set an extension
        """
        pass

    def add_extension(self, number:str, first_name:str, last_name:Optional[str]=None, email:Optional[str]=None, mobile:Optional[str]=None,outb_call_id:Optional[str]=None,voice_mail_enabled:Optional[bool]=False,accept_multiple_calls:Optional[bool]=False) -> dict:
        """
        Add an extension

        :param number: Extension number required
        :param first_name: First name required
        :param last_name: Last name Optional
        :param email: Email Optional
        :param mobile: Cell phone Optional
        :param outb_call_id: Outbound caller id Optional
        :param voice_mail_enabled: Voice mail enabled Optional (default: False)
        :param accept_multiple_calls: Accept multiple calls Optional (default: False)
        """

        response = self.post("ExtensionList/new", payload={}).json()
        ObjectId = str(response['Id'])

        self.update(ObjectId,"Number",number)
        self.update(ObjectId,"FirstName",first_name)
        if last_name:
            self.update(ObjectId,"LastName",last_name)
        if email:
            self.update(ObjectId,"Email",email)
        if mobile:
            self.update(ObjectId,"MobileNumber",mobile)
        if outb_call_id:
            self.update(ObjectId,"OutboundCallerId",outb_call_id)
        if voice_mail_enabled:
            self.update(ObjectId,"VMEnabled",voice_mail_enabled)
        if accept_multiple_calls:
            self.update(ObjectId,["ForwardingAvailable","AcceptMultipleCalls"],accept_multiple_calls)
        

        response = self.save(ObjectId)
        if response.status_code == 200:
            self.logger.info(f"Add Extension {number} - {first_name} {last_name} Successful")
            return response