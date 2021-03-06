#
# (c) Copyright 2015-2017 Hewlett Packard Enterprise Development Company LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#

from eon.common import exception
_FATAL_EXCEPTION_FORMAT_ERRORS = False


class HlmFacadeException(exception.EonException):
    message = _("%s")


class CobblerException(exception.EonException):
    message = _("%s")


class TimeoutError(exception.EonException):
    message = _("%s")


class GetException(exception.EonException):
    message = _("%s")


class UpdateException(exception.EonException):
    message = _("%s")


class Unauthorized(exception.EonException):
    message = _("Unauthorized: token is invalid")


class NotFound(exception.EonException):
    message = _("%s")


class RetryException(exception.EonException):

    def __init__(self, cleanup=None):
        self.cleanup = cleanup
        self.message = _("Retrying input model state change.")
