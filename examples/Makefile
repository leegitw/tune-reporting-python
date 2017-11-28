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

example-v2-advertisers:
	@echo "======================================================"
	@echo example-v2-advertisers
	@echo "======================================================"
	$(PYTHON3) example_tune_v2_advertisers.py $(tmc_api_key)

example-v2-advertiser-sites:
	@echo "======================================================"
	@echo example-v2-advertiser-sites
	@echo "======================================================"
	$(PYTHON3) example_tune_v2_advertiser_sites.py $(tmc_api_key)

example-v2-actuals-find:
	@echo "======================================================"
	@echo example-v2-actuals-find
	@echo "======================================================"
	$(PYTHON3) example_tune_v2_advertiser_stats_actuals_find.py $(tmc_api_key)

example-v2-actuals-export-download:
	@echo "======================================================"
	@echo example-v2-actuals-export-download
	@echo "======================================================"
	$(PYTHON3) example_tune_v2_advertiser_stats_actuals_export_download.py $(tmc_api_key)

example-v2-actuals-export-stream-csv:
	@echo "======================================================"
	@echo example-v2-actuals-export-stream-csv
	@echo "======================================================"
	$(PYTHON3) example_tune_v2_advertiser_stats_actuals_export_stream_csv.py $(tmc_api_key)

example-v2-actuals-export-stream-csv-transform:
	@echo "======================================================"
	@echo example-v2-actuals-export-stream-csv-transform
	@echo "======================================================"
	$(PYTHON3) example_tune_v2_advertiser_stats_actuals_export_stream_csv_transform.py $(tmc_api_key)

example-v3-clicks-find:
	@echo "======================================================"
	@echo example-v3-clicks-find
	@echo "======================================================"
	$(PYTHON3) example_tune_v3_logs_advertisers_clicks_find.py $(tmc_api_key)

example-v3-clicks-export:
	@echo "======================================================"
	@echo example-v3-clicks-export
	@echo "======================================================"
	$(PYTHON3) example_tune_v3_logs_advertisers_clicks_export.py $(tmc_api_key)

example-v3-impressions-find:
	@echo "======================================================"
	@echo example-v3-impressions-find
	@echo "======================================================"
	$(PYTHON3) example_tune_v3_logs_advertisers_impressions_find.py $(tmc_api_key)

example-v3-impressions-export:
	@echo "======================================================"
	@echo example-v3-impressions-export
	@echo "======================================================"
	$(PYTHON3) example_tune_v3_logs_advertisers_impressions_export.py $(tmc_api_key)

example_tune_v2_advertisers:
	@echo "======================================================"
	@echo example_tune_v2_advertisers
	@echo "======================================================"
	$(PYTHON3) example_tune_v2_advertisers.py $(tmc_api_key)

example_tune_v2_session_authenticate:
	@echo "======================================================"
	@echo example_tune_v2_session_authenticate
	@echo "======================================================"
	$(PYTHON3) example_tune_v2_session_authenticate.py $(tmc_api_key)

run-examples:
	@echo "======================================================"
	@echo run-examples
	@echo "======================================================"
	@for example in $(PACKAGE_EXAMPLE_FILES); do \
		echo "======================================================" ; \
		echo Example $$example ; \
		echo "======================================================" ; \
		$(PYTHON3) $$example $(tmc_api_key) ; \
	done

