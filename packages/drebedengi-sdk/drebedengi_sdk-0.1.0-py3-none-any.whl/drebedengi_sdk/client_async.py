"""
Asynchronous SOAP client for Drebedengi.ru API.
"""

from zeep import AsyncClient, exceptions as zeep_exceptions
from zeep.transports import AsyncTransport
from aiohttp import ClientSession, ClientError

from .logger import logger
from .exceptions import DrebedengiError, DrebedengiConnectionError, DrebedengiAPIError


class DrebedengiAsyncAPI:
    """
    Async client for interacting with Drebedengi.ru SOAP API.
    """

    def __init__(self, api_id: str, login: str, password: str):
        """
        Initialize the async client.

        :param api_id: API ID from the user profile.
        :param login: User login (email).
        :param password: User password.
        """
        self.api_id = api_id
        self.login = login
        self.password = password
        self.wsdl = 'https://www.drebedengi.ru/soap/dd.wsdl'
        self.session = ClientSession()
        self.transport = AsyncTransport(session=self.session)
        self.client = None

    async def init_client(self):
        """
        Initialize the SOAP client asynchronously.
        """
        self.client = await AsyncClient(wsdl=self.wsdl, transport=self.transport)
        logger.info("Async Drebedengi client initialized")

    async def close(self):
        """
        Close the aiohttp session.
        """
        await self.session.close()

    async def _call_method(self, method_name, *args):
        """
        Internal method for making authenticated SOAP calls.

        :param method_name: SOAP method name.
        :param args: Arguments passed to the method.
        :return: API response.
        """
        try:
            logger.debug(f"[Async] Calling {method_name} with args: {args}")
            method = getattr(self.client.service, method_name)
            result = await method(self.api_id, self.login, self.password, *args)
            logger.debug(f"[Async] Result from {method_name}: {result}")
            return result
        except zeep_exceptions.Fault as fault:
            logger.error(f"[Async] API Fault in {method_name}: {fault}")
            raise DrebedengiAPIError(f"API Fault: {fault}")
        except ClientError as e:
            logger.error(f"[Async] Connection error: {e}")
            raise DrebedengiConnectionError(str(e))
        except Exception as e:
            logger.error(f"[Async] Unexpected error in {method_name}: {e}")
            raise DrebedengiError(str(e))

    # === API METHODS ===

    async def delete_all(self):
        """
        Asynchronously delete all user data.

        :return: API response.
        """
        return await self._call_method("deleteAll")

    async def delete_object(self, id, type):
        """
        Asynchronously delete an object by ID and type.

        :param id: Object ID.
        :param type: Object type.
        :return: API response.
        """
        return await self._call_method("deleteObject", id, type)

    async def get_access_status(self):
        """
        Asynchronously get the current access status for the user.

        :return: Current access status.
        """
        return await self._call_method("getAccessStatus")

    async def get_accum_list(self, id_list=None):
        """
        Asynchronously get the accumulation list.

        :param id_list: Optional list of IDs.
        :return: Accumulation list.
        """
        return await self._call_method("getAccumList", id_list)

    async def get_check_list(self, id_list=None):
        """
        Asynchronously get the list of checks.

        :param id_list: Optional list of IDs.
        :return: List of checks.
        """
        return await self._call_method("getCheckList", id_list)

    async def get_check_to_record_list(self, id_list=None):
        """
        Asynchronously get the check-to-record mappings.

        :param id_list: Optional list of IDs.
        :return: Check-to-record mappings.
        """
        return await self._call_method("getCheckToRecordList", id_list)

    async def get_balance(self, params=None):
        """
        Asynchronously get account balance data.

        :param params: Optional parameters for the request.
        :return: Account balance data.
        """
        return await self._call_method("getBalance", params)

    async def get_category_list(self, id_list=None):
        """
        Asynchronously get the list of categories.

        :param id_list: Optional list of IDs.
        :return: List of categories.
        """
        return await self._call_method("getCategoryList", id_list)

    async def get_change_list(self, revision):
        """
        Asynchronously get the list of changes since the given revision.

        :param revision: Revision number.
        :return: List of changes.
        """
        return await self._call_method("getChangeList", revision)

    async def get_currency_list(self, id_list=None):
        """
        Asynchronously get the list of currencies.

        :param id_list: Optional list of IDs.
        :return: List of currencies.
        """
        return await self._call_method("getCurrencyList", id_list)

    async def get_current_revision(self):
        """
        Asynchronously get the current revision number.

        :return: Current revision number.
        """
        return await self._call_method("getCurrentRevision")

    async def get_expire_date(self):
        """
        Asynchronously get the subscription expiration date.

        :return: Subscription expiration date.
        """
        return await self._call_method("getExpireDate")

    async def get_order_list(self, id_list=None):
        """
        Asynchronously get the list of orders.

        :param id_list: Optional list of IDs.
        :return: List of orders.
        """
        return await self._call_method("getOrderList", id_list)

    async def get_place_list(self, id_list=None):
        """
        Asynchronously get the list of places (e.g., shops).

        :param id_list: Optional list of IDs.
        :return: List of places.
        """
        return await self._call_method("getPlaceList", id_list)

    async def get_record_list(self, params=None, id_list=None):
        """
        Asynchronously get the list of financial records (transactions).

        :param params: Optional parameters for the request.
        :param id_list: Optional list of IDs.
        :return: List of financial records.
        """
        return await self._call_method("getRecordList", params, id_list)

    async def get_right_access(self):
        """
        Asynchronously get user access rights.

        :return: User access rights.
        """
        return await self._call_method("getRightAccess")

    async def get_server_subs(self, url):
        """
        Asynchronously get server subscriptions for the given URL.

        :param url: Webhook URL.
        :return: Server subscriptions.
        """
        try:
            method = getattr(self.client.service, "getServerSubs")
            return await method(url)
        except Exception as e:
            logger.error(f"[Async] getServerSubs failed: {e}")
            raise DrebedengiError(str(e))

    async def get_source_list(self, id_list=None):
        """
        Asynchronously get the list of income sources.

        :param id_list: Optional list of IDs.
        :return: List of income sources.
        """
        return await self._call_method("getSourceList", id_list)

    async def get_subscription_status(self):
        """
        Asynchronously get the current subscription status.

        :return: Subscription status.
        """
        return await self._call_method("getSubscriptionStatus")

    async def get_tag_list(self, id_list=None):
        """
        Asynchronously get the list of tags.

        :param id_list: Optional list of IDs.
        :return: List of tags.
        """
        return await self._call_method("getTagList", id_list)

    async def get_user_id_by_login(self):
        """
        Asynchronously get the user ID from the login (email).

        :return: User ID.
        """
        return await self._call_method("getUserIdByLogin")

    async def parse_text_data(self, def_place_from_id, def_cat_id, def_src_id, def_place_to_id, list_):
        """
        Asynchronously parse text data into structured financial records.

        :param def_place_from_id: Default place from ID.
        :param def_cat_id: Default category ID.
        :param def_src_id: Default source ID.
        :param def_place_to_id: Default place to ID.
        :param list_: List of text data.
        :return: Parsed financial records.
        """
        return await self._call_method(
            "parseTextData", def_place_from_id, def_cat_id, def_src_id, def_place_to_id, list_
        )

    async def parse_push_data(self, list_):
        """
        Asynchronously parse push notifications into structured records.

        :param list_: List of push data.
        :return: Parsed records.
        """
        return await self._call_method("parsePushData", list_)

    async def set_accum_list(self, list_):
        """
        Asynchronously set the accumulation list.

        :param list_: List of accumulations.
        :return: API response.
        """
        return await self._call_method("setAccumList", list_)

    async def set_category_list(self, list_):
        """
        Asynchronously set the category list.

        :param list_: List of categories.
        :return: API response.
        """
        return await self._call_method("setCategoryList", list_)

    async def set_currency_list(self, list_):
        """
        Asynchronously set the currency list.

        :param list_: List of currencies.
        :return: API response.
        """
        return await self._call_method("setCurrencyList", list_)

    async def set_payment_transaction(self, transaction_receipt, amount):
        """
        Asynchronously register a payment transaction.

        :param transaction_receipt: Transaction receipt.
        :param amount: Transaction amount.
        :return: API response.
        """
        return await self._call_method("setPaymentTransaction", transaction_receipt, amount)

    async def set_place_list(self, list_):
        """
        Asynchronously set the list of places.

        :param list_: List of places.
        :return: API response.
        """
        return await self._call_method("setPlaceList", list_)

    async def set_check_list(self, list_):
        """
        Asynchronously set the check list.

        :param list_: List of checks.
        :return: API response.
        """
        return await self._call_method("setCheckList", list_)

    async def set_check_to_record_list(self, list_):
        """
        Asynchronously set the check-to-record mappings.

        :param list_: List of mappings.
        :return: API response.
        """
        return await self._call_method("setCheckToRecordList", list_)

    async def set_record_list(self, list_):
        """
        Asynchronously set the list of financial records.

        :param list_: List of financial records.
        :return: API response.
        """
        return await self._call_method("setRecordList", list_)

    async def set_source_list(self, list_):
        """
        Asynchronously set the list of income sources.

        :param list_: List of income sources.
        :return: API response.
        """
        return await self._call_method("setSourceList", list_)

    async def set_tag_list(self, list_):
        """
        Asynchronously set the list of tags.

        :param list_: List of tags.
        :return: API response.
        """
        return await self._call_method("setTagList", list_)

    async def user_register(self, name, lang):
        """
        Asynchronously register a new user.

        :param name: Username.
        :param lang: Preferred language.
        :return: API response.
        """
        return await self._call_method("userRegister", name, lang)