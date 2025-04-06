from zeep import Client, exceptions as zeep_exceptions
from zeep.transports import Transport
from requests import Session, RequestException

from .logger import logger
from .exceptions import DrebedengiError, DrebedengiConnectionError, DrebedengiAPIError


class DrebedengiAPI:
    """
    A client for accessing Drebedengi.ru SOAP API.
    """

    def __init__(self, api_id: str, login: str, password: str):
        """
        Initialize the Drebedengi SOAP client.

        :param api_id: API ID from the user's profile.
        :param login: User login (email).
        :param password: User password.
        """
        self.api_id = api_id
        self.login = login
        self.password = password
        self.wsdl = 'https://www.drebedengi.ru/soap/dd.wsdl'
        session = Session()
        self.client = Client(self.wsdl, transport=Transport(session=session))
        logger.info("Drebedengi client initialized")

    def _call_method(self, method_name, *args):
        """
        Internal method for invoking SOAP API calls.

        :param method_name: Name of the SOAP method.
        :param args: Arguments to pass to the method.
        :return: API response.
        """
        try:
            logger.debug(f"Calling method {method_name} with args: {args}")
            method = getattr(self.client.service, method_name)
            result = method(self.api_id, self.login, self.password, *args)
            logger.debug(f"Result from {method_name}: {result}")
            return result
        except zeep_exceptions.Fault as fault:
            logger.error(f"API Fault on {method_name}: {fault}")
            raise DrebedengiAPIError(f"API Fault: {fault}")
        except RequestException as e:
            logger.error(f"Connection error: {e}")
            raise DrebedengiConnectionError(str(e))
        except Exception as e:
            logger.error(f"Unexpected error in {method_name}: {e}")
            raise DrebedengiError(str(e))

    def delete_all(self):
        """Delete all user data."""
        return self._call_method("deleteAll")

    def delete_object(self, id, type):
        """
        Delete an object by ID and type.

        :param id: Object ID.
        :param type: Object type.
        """
        return self._call_method("deleteObject", id, type)

    def get_access_status(self):
        """Get current access status for the user."""
        return self._call_method("getAccessStatus")

    def get_accum_list(self, id_list=None):
        """Get accumulation list."""
        return self._call_method("getAccumList", id_list)

    def get_check_list(self, id_list=None):
        """Get list of checks."""
        return self._call_method("getCheckList", id_list)

    def get_check_to_record_list(self, id_list=None):
        """Get check-to-record mappings."""
        return self._call_method("getCheckToRecordList", id_list)

    def get_balance(self, params=None):
        """Get account balance data."""
        return self._call_method("getBalance", params)

    def get_category_list(self, id_list=None):
        """Get list of categories."""
        return self._call_method("getCategoryList", id_list)

    def get_change_list(self, revision):
        """Get list of changes since the given revision."""
        return self._call_method("getChangeList", revision)

    def get_currency_list(self, id_list=None):
        """Get list of currencies."""
        return self._call_method("getCurrencyList", id_list)

    def get_current_revision(self):
        """Get current revision number."""
        return self._call_method("getCurrentRevision")

    def get_expire_date(self):
        """Get subscription expiration date."""
        return self._call_method("getExpireDate")

    def get_order_list(self, id_list=None):
        """Get list of orders."""
        return self._call_method("getOrderList", id_list)

    def get_place_list(self, id_list=None):
        """Get list of places (e.g., shops)."""
        return self._call_method("getPlaceList", id_list)

    def get_record_list(self, params=None, id_list=None):
        """Get list of financial records (transactions)."""
        return self._call_method("getRecordList", params, id_list)

    def get_right_access(self):
        """Get user access rights."""
        return self._call_method("getRightAccess")

    def get_server_subs(self, url):
        """
        Get server subscriptions for the given URL.

        :param url: Webhook URL.
        """
        try:
            return self.client.service.getServerSubs(url)
        except Exception as e:
            raise DrebedengiError(str(e))

    def get_source_list(self, id_list=None):
        """Get list of income sources."""
        return self._call_method("getSourceList", id_list)

    def get_subscription_status(self):
        """Get current subscription status."""
        return self._call_method("getSubscriptionStatus")

    def get_tag_list(self, id_list=None):
        """Get list of tags."""
        return self._call_method("getTagList", id_list)

    def get_user_id_by_login(self):
        """Get user ID from login (email)."""
        return self._call_method("getUserIdByLogin")

    def parse_text_data(self, def_place_from_id, def_cat_id, def_src_id, def_place_to_id, list_):
        """Parse text data into structured financial records."""
        return self._call_method("parseTextData", def_place_from_id, def_cat_id, def_src_id, def_place_to_id, list_)

    def parse_push_data(self, list_):
        """Parse push notifications into structured records."""
        return self._call_method("parsePushData", list_)

    def set_accum_list(self, list_):
        """Set accumulation list."""
        return self._call_method("setAccumList", list_)

    def set_category_list(self, list_):
        """Set category list."""
        return self._call_method("setCategoryList", list_)

    def set_currency_list(self, list_):
        """Set currency list."""
        return self._call_method("setCurrencyList", list_)

    def set_payment_transaction(self, transaction_receipt, amount):
        """Set payment transaction with receipt and amount."""
        return self._call_method("setPaymentTransaction", transaction_receipt, amount)

    def set_place_list(self, list_):
        """Set list of places."""
        return self._call_method("setPlaceList", list_)

    def set_check_list(self, list_):
        """Set check list."""
        return self._call_method("setCheckList", list_)

    def set_check_to_record_list(self, list_):
        """Set check-to-record mappings."""
        return self._call_method("setCheckToRecordList", list_)

    def set_record_list(self, list_):
        """Set list of financial records."""
        return self._call_method("setRecordList", list_)

    def set_source_list(self, list_):
        """Set list of income sources."""
        return self._call_method("setSourceList", list_)

    def set_tag_list(self, list_):
        """Set list of tags."""
        return self._call_method("setTagList", list_)

    def user_register(self, name, lang):
        """
        Register a new user.

        :param name: Username.
        :param lang: Preferred language.
        """
        return self._call_method("userRegister", name, lang)
