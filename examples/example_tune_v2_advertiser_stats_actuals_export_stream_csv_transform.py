#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

import os
import sys
from pprintpp import pprint
from datetime import datetime, timedelta
import pytz
import ujson as json
import logging

from requests_mv_integrations.exceptions import (TuneRequestBaseError)
from tune_reporting.errors import (print_traceback, get_exception_message)
from tune_reporting.exceptions import (TuneReportingError)
from tune_reporting.tmc.v2.reporting import (
    TuneV2AdvertiserStatsActuals,
    TuneV2AdvertiserStatsFormats
)
from tune_reporting.support import convert_size
from tune_reporting.tmc.v2.management import (TuneV2AuthenticationTypes)
from logging_mv_integrations import (LoggingFormat, LoggingOutput)
from safe_cast import (safe_str, safe_float, safe_int)


def main(tmc_api_key):

    TIMEZONE_COLLECT = "America/New_York"

    tune_v2_advertiser_stats_actuals = \
        TuneV2AdvertiserStatsActuals(
            timezone=TIMEZONE_COLLECT,
            logger_level=logging.INFO,
            logger_format=LoggingFormat.JSON,
            logger_output=LoggingOutput.STDOUT_COLOR
        )

    dw_file_path = "data.{}".format(TuneV2AdvertiserStatsFormats.JSON)
    if os.path.exists(dw_file_path):
        os.remove(dw_file_path)

    tz = pytz.timezone(TIMEZONE_COLLECT)
    yesterday = datetime.now(tz).date() - timedelta(days=1)
    str_yesterday = str(yesterday)

    request_params = {
        'format': TuneV2AdvertiserStatsFormats.CSV,
        'fields': (
            "ad_clicks,"
            "ad_clicks_unique,"
            "ad_impressions,"
            "ad_impressions_unique,"
            "ad_network_id,"
            "advertiser_id,"
            "country.code,"
            "date_hour,"
            "events,"
            "installs,"
            "is_reengagement,"
            "payouts,"
            "publisher_id,"
            "publisher_sub_ad.ref,"
            "publisher_sub_adgroup.ref,"
            "publisher_sub_campaign.ref,"
            "publisher_sub_publisher.ref,"
            "publisher_sub_site.ref,"
            "site_id"
        ),
        'group': (
            "country_id,"
            "is_reengagement,"
            "publisher_id,"
            "publisher_sub_ad_id,"
            "publisher_sub_adgroup_id,"
            "publisher_sub_campaign_id,"
            "publisher_sub_publisher_id,"
            "publisher_sub_site_id,"
            "site_id"
        ),
        'timezone': "America/Los_Angeles"
    }

    try:
        tune_v2_advertiser_stats_actuals.tmc_auth(tmc_api_key=tmc_api_key)

        response = tune_v2_advertiser_stats_actuals.stream(
            auth_value=tmc_api_key,
            auth_type=TuneV2AuthenticationTypes.API_KEY,
            auth_type_use=TuneV2AuthenticationTypes.API_KEY,
            start_date=str_yesterday,
            end_date=str_yesterday,
            request_params=request_params,
            request_retry={'delay': 15,
                           'timeout': 30,
                           'tries': 5}
        )

        line_count = 0

        csv_keys_list = None

        json_keys_dict = {
            "publisher_sub_campaign.ref": "sub_campaign_ref",
            "publisher_sub_ad.ref": "sub_ad_ref",
            "publisher_sub_adgroup.ref": "sub_adgroup_ref",
            "publisher_sub_publisher.ref": "sub_publisher_ref",
            "publisher_sub_site.ref": "sub_site_ref",
            "publisher_sub_placement.ref": "sub_placement_ref",
            "publisher_sub_campaign.name": "sub_campaign_name",
            "publisher_sub_ad.name": "sub_ad_name",
            "publisher_sub_adgroup.name": "sub_adgroup_name",
            "publisher_sub_publisher.name": "sub_publisher_name",
            "publisher_sub_site.name": "sub_site_name",
            "publisher_sub_placement.name": "sub_placement_name",
            "publisher_sub_campaign_id": "sub_campaign_id",
            "publisher_sub_ad_id": "sub_ad_id",
            "publisher_sub_adgroup_id": "sub_adgroup_id",
            "publisher_sub_publisher_id": "sub_publisher_id",
            "publisher_sub_site_id": "sub_site_id",
            "publisher_sub_placement_id": "publisher_sub_placement_id",
            "country.code": "country_code",
            "ad_impressions": "received_impressions_gross",
            "ad_impressions_unique": "received_impressions_unique",
            "ad_clicks": "received_clicks_gross",
            "ad_clicks_unique": "received_clicks_unique",
            "events": "received_engagements",
            "installs": "received_installs",
            "payouts": "cost"
        }

        json_types_dict = {
            "client_id": int,
            "partner_id": int,
            "vendor_id": int,
            "date": str,
            "hour": int,
            "timezone": str,
            "granularity": str,
            "site_ref_id": str,
            "site_ref_type": str,
            "partner_ref_id": int,
            "partner_ref_type": str,
            "partner_vendor_ref_id": int,
            "partner_vendor_ref_type": str,
            "sub_campaign_type": str,
            "sub_campaign_ref": str,
            "sub_ad_ref": str,
            "sub_adgroup_ref": str,
            "sub_publisher_ref": str,
            "sub_site_ref": str,
            "sub_placement_ref": str,
            "sub_campaign_name": str,
            "sub_ad_name": str,
            "sub_adgroup_name": str,
            "sub_publisher_name": str,
            "sub_site_name": str,
            "sub_placement_name": str,
            "sub_campaign_name": str,
            "sub_ad_name": str,
            "sub_adgroup_name": str,
            "sub_publisher_name": str,
            "sub_site_name": str,
            "sub_placement_name": str,
            "sub_campaign_id": int,
            "sub_ad_id": int,
            "sub_adgroup_id": int,
            "sub_publisher_id": int,
            "sub_site_id": int,
            "publisher_sub_placement_id": int,
            "country_code": str,
            "received_impressions_gross": int,
            "received_impressions_unique": int,
            "received_clicks_gross": int,
            "received_clicks_unique": int,
            "received_installs": int,
            "received_engagements": int,
            "received_conversions": int,
            "cost": float,
            "cost_currency": str,
            "site_id": int,
            "publisher_id": int,
            "advertiser_id": int,
            "ad_network_id": int,
            "ad_impressions": int,
        }

        client_id = 0
        partner_id = 0
        vendor_id = 0

        timezone = "TBD"
        granularity = "TBD"

        config_extra = {
            "client_id": client_id,
            "partner_id": partner_id,
            "vendor_id": vendor_id,
            "timezone": timezone,
            "granularity": granularity,
            "cost_currency": "USD",
            "received_conversions": 0,
            "site_ref_type": "tmc",
            "partner_ref_type": "tmc",
            "partner_vendor_ref_type": "tmc"
        }

        with open(file=dw_file_path, mode='w') as dw_file_w:
            for bytes_line in response.iter_lines(chunk_size=4096):
                if bytes_line:  # filter out keep-alive new chunks
                    line_count += 1
                    str_line = bytes_line.decode("utf-8")

                    if line_count == 1:
                        csv_keys_list = str_line.split(',')

                        for index, csv_key in enumerate(csv_keys_list):
                            if csv_key in json_keys_dict:
                                csv_keys_list[index] = json_keys_dict[csv_key]
                        continue
                    elif line_count > 2:
                        dw_file_w.write('\n')

                    csv_values_list = str_line.split(',')
                    json__dict = {}

                    is_reengagement = 0
                    received_installs = 0
                    received_engagements = 0

                    for csv_key, csv_value in zip(csv_keys_list, csv_values_list):
                        csv_value_strip = csv_value.strip('"')

                        if csv_key == "date_hour":
                            parts_date_time = csv_value_strip.split(" ")
                            rdate_yyyy_mm_dd = parts_date_time[0]

                            parts_time = parts_date_time[1].split(":")
                            rhour = safe_int(parts_time[0])

                            json__dict.update({"date": rdate_yyyy_mm_dd})

                            json__dict.update({"hour": rhour})
                        elif csv_key == "is_reengagement":
                            is_reengagement = safe_int(csv_value_strip)

                        elif csv_key == "received_installs":
                            received_installs = safe_int(csv_value_strip)
                            json__dict.update({'received_installs': received_installs})

                        elif csv_key == "received_engagements":
                            received_engagements = safe_int(csv_value_strip)
                            json__dict.update({'received_engagements': received_engagements})

                        else:
                            if csv_key in json_types_dict:
                                if json_types_dict[csv_key] == str:
                                    csv_value_typed = safe_str(csv_value_strip)
                                elif json_types_dict[csv_key] == int:
                                    csv_value_typed = safe_int(csv_value_strip)
                                elif json_types_dict[csv_key] == float:
                                    csv_value_typed = safe_float(csv_value_strip)
                                else:
                                    csv_value_typed = safe_str(csv_value_strip)
                            else:
                                csv_value_typed = safe_str(csv_value_strip)

                            json__dict.update({csv_key: csv_value_typed})

                    if is_reengagement == 1:
                        engagements = received_engagements
                    else:
                        engagements = 0

                    if engagements > 0 and received_installs > 0:
                        sub_campaign_type = "acquisition_engagement"
                    elif received_installs > 0:
                        sub_campaign_type = "acquisition"
                    elif engagements > 0:
                        sub_campaign_type = "engagement"
                    else:
                        sub_campaign_type = ""

                    json__dict.update({'sub_campaign_type': sub_campaign_type})

                    json__dict.update(config_extra)

                    json_str = json.dumps(json__dict)
                    dw_file_w.write(json_str)
                dw_file_w.flush()

        statinfo = os.stat(dw_file_path)
        extra = {
            'response_status_code': response.status_code,
            'response_headers': response.headers,
            'dw_file_path': dw_file_path,
            'dw_file_size': convert_size(statinfo.st_size),
            'line_count': line_count,
            'csv_header_list': csv_keys_list
        }

        pprint(extra)

    except TuneRequestBaseError as tmc_req_ex:
        print_traceback(tmc_req_ex)
        pprint(tmc_req_ex.to_dict())
        print(str(tmc_req_ex))

    except TuneReportingError as tmc_rep_ex:
        pprint(tmc_rep_ex.to_dict())
        print(str(tmc_rep_ex))

    except Exception as ex:
        print_traceback(ex)
        print(get_exception_message(ex))


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError("{} [tmc_api_key].".format(sys.argv[0]))
        tmc_api_key = sys.argv[1]
        sys.exit(main(tmc_api_key))
    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise
