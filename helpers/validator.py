from rest_framework import (
    request,
    serializers,
    status
)
from enum import Enum
from django.utils.translation import gettext as _
from django.core import validators

class AvailableTypes(Enum):
    Integer = 1
    String = 2
    Floot = 3
    Boolean = 4
    List = 5

def check(
        key: str,
        type: AvailableTypes,
        request: request.Request,
        max_count: int = None,
        min_count: int = None,
        is_email: bool = False,
        is_password: bool = False
):
    # Data Check 
    data = request.data
    result = data.get(key)
    if (result is None):
        params = request.query_params
        result = params.get(key)
        if (not result):
            raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _(f'{key} field is required')
                },
                code=status.HTTP_400_BAD_REQUEST
            )
    # Type Conversion
    try:
        if type == AvailableTypes.String:
            result = str(result)
            # Min and Maxmimum count check
            if min_count:
                if len(result) < min_count:
                    raise serializers.ValidationError(
                        detail={
                            'status_code': _('0'),
                            'status_message': _(f'{key} should be min {min_count} char')
                        },
                        code=status.HTTP_400_BAD_REQUEST
                    )
            if max_count:
                if len(result) > max_count:
                    raise serializers.ValidationError(
                        detail={
                            'status_code': _('0'),
                            'status_message': _(f'{key} should be less than max {max_count} char')
                        },
                        code=status.HTTP_400_BAD_REQUEST
                    )
            if is_email:
                validators.validate_email(result)
            if is_password:
                pass
        elif type == AvailableTypes.Boolean:
            result = bool(result)
        elif type == AvailableTypes.List:
            result = list(result)
        elif type == AvailableTypes.Integer:
            result = int(result)
            if min_count:
                if result > min_count:
                    raise serializers.ValidationError(
                        detail={
                            'status_code': _('0'),
                            'status_message': _(f'{key} should be min {min_count}')
                        },
                        code=status.HTTP_400_BAD_REQUEST
                    )
            if max_count:
                if result < max_count:
                    raise serializers.ValidationError(
                        detail={
                            'status_code': _('0'),
                            'status_message': _(f'{key} should be max {max_count}')
                        },
                        code=status.HTTP_400_BAD_REQUEST
                    )
        elif type == AvailableTypes.Floot:
            result = float(result)
            if min_count:
                if result > min_count:
                    raise serializers.ValidationError(
                        detail={
                            'status_code': _('0'),
                            'status_message': _(f'{key} should be min {min_count}')
                        },
                        code=status.HTTP_400_BAD_REQUEST
                    )
            if max_count:
                if result < max_count:
                    raise serializers.ValidationError(
                        detail={
                            'status_code': _('0'),
                            'status_message': _(f'{key} should be max {max_count}')
                        },
                        code=status.HTTP_400_BAD_REQUEST
                    )
    except ValueError:
        raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _(f'{key} invalid format')
                },
                code=status.HTTP_400_BAD_REQUEST
            )
    except Exception as e:
        raise serializers.ValidationError(
                detail={
                    'status_code': _('0'),
                    'status_message': _(f'{key} unknown error:: {str(e)}')
                },
                code=status.HTTP_400_BAD_REQUEST
            )
    return result

