# All urls from app accounts
LOGIN_POST = ("login", "post")
LOGIN_REFRESH_POST = ("login_refresh", "post")
FORGOT_PASSWORD_POST = ("forgot_password", "post")
VERIFY_OTP_POST = ("verify_otp", "post")

CUSTOMER_USER_LOGIN_CREATE = ("customer-user-login-list", "post")
ADMIN_USER_LOGIN_CREATE = ("admin-user-login-list", "post")

REGISTER_LIST = ("user-register-list", "get")
REGISTER_READ = ("user-register-detail", "get")
REGISTER_CREATE = ("user-register-list", "post")
REGISTER_UPDATE = ("user-register-detail", "put")
REGISTER_PATCH = ("user-register-detail", "patch")
REGISTER_DELETE = ("user-register-detail", "delete")

CHANGE_PASSWORD_CREATE = ("change_password-list", "post")
RESET_PASSWORD_CREATE = ("reset_password-list", "post")

PROFILE_LIST = ("profile-list", "get")
PROFILE_READ = ("profile-detail", "get")
PROFILE_CREATE = ("profile-list", "post")
PROFILE_UPDATE = ("profile-detail", "put")
PROFILE_PATCH = ("profile-detail", "patch")
PROFILE_DELETE = ("profile-detail", "delete")

BANNERIMG_LIST = ("banner-img-list", "get")
BANNERIMG_READ = ("banner-img-detail", "get")
BANNERIMG_CREATE = ("banner-img-list", "post")
BANNERIMG_UPDATE = ("banner-img-detail", "put")
BANNERIMG_PATCH = ("banner-img-detail", "patch")
BANNERIMG_DELETE = ("banner-img-detail", "delete")


# All urls from app puja

MONASTERIES_LIST = ("monasteries-list", "get")
MONASTERIES_READ = ("monasteries-detail", "get")
MONASTERIES_CREATE = ("monasteries-list", "post")
MONASTERIES_UPDATE = ("monasteries-detail", "put")
MONASTERIES_PATCH = ("monasteries-detail", "patch")
MONASTERIES_DELETE = ("monasteries-detail", "delete")

DISTRICT_SEARCH_LIST = ("search_district-list", "get")
MONASTERY_REGISTER = ('monlam_register-list','post')

PUJAS_LIST = ("pujas-list", "get")
PUJAS_READ = ("pujas-detail", "get")
PUJAS_CREATE = ("pujas-list", "post")
PUJAS_UPDATE = ("pujas-detail", "put")
PUJAS_PATCH = ("pujas-detail", "patch")
PUJAS_DELETE = ("pujas-detail", "delete")


FINANCELOGS_LIST = ("financelogs-list", "get")
FINANCELOGS_READ = ("financelogs-detail", "get")
FINANCELOGS_CREATE = ("financelogs-list", "post")
FINANCELOGS_UPDATE = ("financelogs-detail", "put")
FINANCELOGS_PATCH = ("financelogs-detail", "patch")
FINANCELOGS_DELETE = ("financelogs-detail", "delete")


PUJAREQUESTS_LIST = ("pujarequests-list", "get")
PUJAREQUESTS_READ = ("pujarequests-detail", "get")
PUJAREQUESTS_CREATE = ("pujarequests-list", "post")
PUJAREQUESTS_UPDATE = ("pujarequests-detail", "put")
PUJAREQUESTS_PATCH = ("pujarequests-detail", "patch")
PUJAREQUESTS_DELETE = ("pujarequests-detail", "delete")

GENERATEPDFS_LIST = ("generatepdfs-list", "get")
GENERATEPDFS_CREATE = ("generatepdfs-list", "post")

PUJAREQUESTS_POST = ("pujarequests/request_puja", "post")
PUJAREQUESTS_UPDATE_PATCH = ("pujarequests-update-detail", "patch")

USER_NOTIFICATIION_LIST = ("user-notification-list", "get")
USER_NOTIFICATIION_READ = ("user-notification-detail", "get")
USER_NOTIFICATIION_MARK_AS_READ = ("user-notification-mark-all-as-read", "get")
USER_NOTIFICATIION_LIST_READ = ("user-notification-view-read-notifications", "get")

FCM_DEVICE_REGISTER_CREATE = ("fcm_device_registration-list", "post")

NABIL_PAYMENT_INITIATE = ("nabil_payment_management-initiate", "post")

VERIFY_ESEWA_PAYMENT_POST = ("verify_esewa_payment", "post")
VERIFY_KHALTI_PAYMENT_POST = ("verify_khalti_payment", "post")
ON_NABIL_PAYMENT_SUCCESS = ("nabil_payment_management-success", "post")
NCHL_PAYMENT_INITIATE = ('nchl_payment_management-initiate','post')
UPDATE_MONASTERY = ('monasteries-update-monastery','patch')

NCHL_PAYMENT_FAILURE = ('nchl_payment_failure-list','get')
NCHL_PAYMENT_SUCCESS = ('nchl_payment_success-list','get')

PUJA_TWEAK_CREATE = ('puja_tweak-list','post')