#   Makefile
#
#   Copyright (c) 2017 TUNE, Inc
#   All rights reserved.
#
# license   http://opensource.org/licenses/MIT The MIT License (MIT)
# copyright Copyright (c) 2017 TUNE Inc. (http://www.tune.com)
#

PYTHON3 := $(shell which python3)

PACKAGE_EXAMPLE_FILES := $(shell find . ! -name '__init__.py' -type f -name "*.py")

example_tune_v2_advertisers:
	@echo "======================================================"
	@echo example-v2-advertisers
	@echo "======================================================"
	$(eval export TMC_API_KEY=$(tmc_api_key))
	@printenv | grep TMC_API_KEY
	$(PYTHON3) example_tune_v2_advertisers.py $(tmc_api_key)

example_tune_v2_advertiser_sites:
	@echo "======================================================"
	@echo example_tune_v2_advertiser_sites
	@echo "======================================================"
	$(eval export TMC_API_KEY=$(tmc_api_key))
	@printenv | grep TMC_API_KEY
	$(PYTHON3) example_tune_v2_advertiser_sites.py $(tmc_api_key)

example_tune_v2_advertiser_stats_actuals_find:
	@echo "======================================================"
	@echo example_tune_v2_advertiser_stats_actuals_find
	@echo "======================================================"
	$(eval export TMC_API_KEY=$(tmc_api_key))
	@printenv | grep TMC_API_KEY
	$(PYTHON3) example_tune_v2_advertiser_stats_actuals_find.py $(tmc_api_key)

example_tune_v2_advertiser_stats_actuals_export_download:
	@echo "======================================================"
	@echo example_tune_v2_advertiser_stats_actuals_export_download
	@echo "======================================================"
	$(eval export TMC_API_KEY=$(tmc_api_key))
	@printenv | grep TMC_API_KEY
	$(PYTHON3) example_tune_v2_advertiser_stats_actuals_export_download.py $(tmc_api_key)

example_tune_v2_advertiser_stats_actuals_export_stream_csv:
	@echo "======================================================"
	@echo example_tune_v2_advertiser_stats_actuals_export_stream_csv
	@echo "======================================================"
	$(eval export TMC_API_KEY=$(tmc_api_key))
	@printenv | grep TMC_API_KEY
	$(PYTHON3) example_tune_v2_advertiser_stats_actuals_export_stream_csv.py $(tmc_api_key)

example_tune_v2_advertiser_stats_actuals_export_stream_csv_transform:
	@echo "======================================================"
	@echo example_tune_v2_advertiser_stats_actuals_export_stream_csv_transform
	@echo "======================================================"
	$(eval export TMC_API_KEY=$(tmc_api_key))
	@printenv | grep TMC_API_KEY
	$(PYTHON3) example_tune_v2_advertiser_stats_actuals_export_stream_csv_transform.py $(tmc_api_key)

example_tune_v3_logs_advertisers_clicks_find:
	@echo "======================================================"
	@echo example_tune_v3_logs_advertisers_clicks_find
	@echo "======================================================"
	$(eval export TMC_API_KEY=$(tmc_api_key))
	@printenv | grep TMC_API_KEY
	$(PYTHON3) example_tune_v3_logs_advertisers_clicks_find.py $(tmc_api_key)

example_tune_v3_logs_advertisers_clicks_export:
	@echo "======================================================"
	@echo example_tune_v3_logs_advertisers_clicks_export
	@echo "======================================================"
	$(eval export TMC_API_KEY=$(tmc_api_key))
	@printenv | grep TMC_API_KEY
	$(eval export TMC_API_KEY=$(tmc_api_key))
	@printenv | grep TMC_API_KEY
	$(PYTHON3) example_tune_v3_logs_advertisers_clicks_export.py $(tmc_api_key)

example_tune_v3_logs_advertisers_impressions_find:
	@echo "======================================================"
	@echo example_tune_v3_logs_advertisers_impressions_find
	@echo "======================================================"
	$(eval export TMC_API_KEY=$(tmc_api_key))
	@printenv | grep TMC_API_KEY
	$(PYTHON3) example_tune_v3_logs_advertisers_impressions_find.py $(tmc_api_key)

example_tune_v3_logs_advertisers_impressions_export:
	@echo "======================================================"
	@echo example_tune_v3_logs_advertisers_impressions_export
	@echo "======================================================"
	$(PYTHON3) example_tune_v3_logs_advertisers_impressions_export.py $(tmc_api_key)

example_tune_v2_session_authenticate:
	@echo "======================================================"
	@echo example_tune_v2_session_authenticate
	@echo "======================================================"
	$(eval export TMC_API_KEY=$(tmc_api_key))
	@printenv | grep TMC_API_KEY
	$(PYTHON3) example_tune_v2_session_authenticate.py $(tmc_api_key)

run-examples:
	@echo "======================================================"
	@echo run-examples
	@echo "======================================================"
	$(eval export TMC_API_KEY=$(tmc_api_key))
	@printenv | grep TMC_API_KEY
	@for example in $(PACKAGE_EXAMPLE_FILES); do \
		echo "======================================================" ; \
		echo Example $$example ; \
		echo "======================================================" ; \
		$(PYTHON3) $$example $(tmc_api_key) ; \
	done

list:
	cat Makefile | grep "^[a-z]" | awk '{print $$1}' | sed "s/://g" | sort