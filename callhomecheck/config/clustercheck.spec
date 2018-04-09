[__many__]
	CLUSTER_TOP=string(default="", min=1)
	REMOTE_CHECK_HOME=string(default="")
	ADMIN_USER=string(default="Admin")
	ADMIN_PASS=string(default="Admin")
	LOG_LEVEL=option("NOTSET", "CRIT", "ERROR", "WARN", "INFO", "DEBUG", default="ERROR")
	LOG_DIR=string(default="log")
	WORK_DIR=string(default="work")
	COMPONENTS=option_list(options=list('EGO', 'SYM', 'LSF'), min=1, max=3)
	CHECK_INTERVAL=integer(default=1800, min=0)
	EXIT_CYCLE_ON_FAILURE=yes_no(default="N")
	FAILOVER_WAIT=integer(default=300, min=0)
	CMD_TIMEOUT=integer(default=30, min=0)
	DISABLE_MODE=option('CHECK', 'PROGRAM', default='CHECK')
	SSH_PRIVATE_KEY=string(default="")
	TEST_MODE=yes_no(default="Y")
	[[SNAPSHOT]]
		SNAPSHOT_HOME=string(default='clsnapshot')
		SNAPSHOT_DIR=string(default='snapshots')
		GENERATE_ON_ALERT=yes_no(default="N")	
		INTERVAL=integer(default=1440, min=0)
		RETENTION=integer(default=1, min=0)
	[[EMAIL]]
		ENABLED=yes_no(default="N")
		TO=email_list(default=list())
		FROM=email(default="")
		CONTACT_NAME=string(default="")
		CONTACT_PHONE=string(default="")
		CONTACT_EMAIL=email(default="")
		COMMAND=string(default="")
		SERVER=string(default="localhost:25")
		CUSTOM_MESSAGE=string(default="")
		INCLUDE_UPLOAD_COMMAND=yes_no(default="N")
	[[CALLHOME]]
		ENABLED=yes_no(default="N")
		ECC_JAR=string(default="eccagent.jar")
		ECC_TOP=string(default="ecc")
		ECC_HOST=string(default="localhost")
		ECC_JAVA_HOME=string(default="")
		ECC_TIMEOUT=integer(default=300, min=0)
		ICN=string(default="")
		GROUP=string(default="")
		PHONE=string(default="")
		CUSTOMER_NAME=string(default="")
		EMAIL=email(default="")
		CITY=string(default="")
		COUNTRY=string(default="")
		UUID=string(default="")
		SEVERITY=integer(default=3, min=1, max=4)
		AUTO_UPLOAD=yes_no(default="Y")
		SNAPSHOT_UPLOAD=integer(default=2, min=0)
        SUMMARY_PREFIX=string(default="[CH]")
        LSF_COMPONENT=string(default='IBM/5725G8201')
        LSF_VERSION=string(default='')
        SYM_COMPONENT=string(default='IBM/5725G8601')
        SYM_VERSION=string(default='')
	[[EGO]]
		CMD_TIMEOUT=integer(default=None, min=0)
		[[[CHECKS]]]
			TIMEOUT=integer(default=30, min=0)
			[[[[RESPONSE]]]]
				[[[[[VEMKD]]]]]
					ENABLED=yes_no(default='N')
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					TIMEOUT=integer(default=30, min=0)
				[[[[[EGOSC]]]]]
					ENABLED=yes_no(default="N")
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					TIMEOUT=integer(default=30, min=0)
			[[[[DAEMON]]]]
				[[[[[__many__]]]]]
					ENABLED=yes_no(default="N")
					NAME=string(min=1)
					BINARY=string(min=1)
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					TIMEOUT=integer(default=30, min=0)
					UT_SAMPLING=sample_option(default=list("SAMPLES: 3", "INTERVAL: 1"))
					UT_LIMIT=limit_option(default=list("WARN: 90", "ALERT: 98"))
					MEM_SAMPLING=sample_option(default=list("SAMPLES: 3", "INTERVAL: 1"))
					MEM_LIMIT=limit_option(default=list("WARN: 4000", "ALERT: 5000"))
					FD_LIMIT=limit_option(default=list("WARN: 3900", "ALERT: 4096"))
					FAIL_IF_MISSING=yes_no(default="Y")
					FAIL_IF_RESTARTED=yes_no(default="Y")
					MINIMUM_UPTIME=integer(default=120, min=0)
			[[[[DIR]]]]
				[[[[[__many__]]]]]
					ENABLED=yes_no(default="N")
					NAME=string(min=1)
					DIR=string(min=1)
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					DISK_SPACE_LIMIT=limit_option(default=list("WARN: 5000", "ALERT: 1000"))
					SIZE_LIMIT=limit_option(default=list("WARN: 45000", "ALERT: 50000"))
					TIMEOUT=integer(default=30, min=0)
			[[[[CORE]]]]
				[[[[[__many__]]]]]
					CORE_LIMIT=limit_option(default=list("WARN: 1", "ALERT: 3"))
					# W_LIMIT=string(default="Y")
					#CORE_LIMIT=string(default="Y")
					ENABLED=yes_no(default="N")
					NAME=string(min=1)
					BINARY=string(min=1)
					DIRS=force_string_list(default=list("/tmp"))
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					NAME_FORMAT=string(default="core*.*")
			[[[[EGO_SERVICE]]]]
				[[[[[__many__]]]]]
					NAME=string(min=1)
					ENABLED=yes_no(default="N")
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					TIMEOUT=integer(default=30, min=0)
			[[[[CUSTOM]]]]
				[[[[[__many__]]]]]
					NAME=string(min=1)
					ENABLED=yes_no(default="N")
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					TIMEOUT=integer(default=30, min=0)
					COMMAND=string(min=1)
					SUCCESS_EXIT_CODES=force_int_list(default=0)

	[[SYM]]
		CMD_TIMEOUT=integer(default=None, min=0)
		[[[CHECKS]]]
			[[[[RESPONSE]]]]
				[[[[[SD]]]]]
					NAME=string(default='sd', min=1)
					ENABLED=yes_no(default="N")
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					TIMEOUT=integer(default=30, min=0)
				[[[[[SSM]]]]]
					[[[[[[__many__]]]]]]
						ENABLED=yes_no(default="N")
						FAIL_LIMIT=integer(default=3, min=1)
						WARN_LIMIT=integer(default=0, min=0)
						RETRY_IMMEDIATELY=yes_no(default="Y")
						RETRY_WAIT_TIME=integer(default=0, min=0)
						TIMEOUT=integer(default=30, min=0)
						APPLICATION=string(min=1)
						NAME=string(min=1)
			[[[[DAEMON]]]]
				[[[[[SD]]]]]
					ENABLED=yes_no(default="N")
					NAME=string(default='sd', min=1)
					BINARY=string(default='sd', min=1)
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					TIMEOUT=integer(default=30, min=0)
					UT_SAMPLING=sample_option(default=list("SAMPLES: 3", "INTERVAL: 1"))
					UT_LIMIT=limit_option(default=list("WARN: 90", "ALERT: 98"))
					MEM_SAMPLING=sample_option(default=list("SAMPLES: 3", "INTERVAL: 1"))
					MEM_LIMIT=limit_option(default=list("WARN: 4000", "ALERT: 5000"))
					FD_LIMIT=limit_option(default=list("WARN: 3900", "ALERT: 4096"))
					FAIL_IF_MISSING=yes_no(default="Y")
					FAIL_IF_RESTARTED=yes_no(default="Y")
					MINIMUM_UPTIME=integer(default=120, min=0)
				[[[[[SSM]]]]]
					[[[[[[__many__]]]]]]
						ENABLED=yes_no(default="N")
						APPLICATION=string(min=1)
						NAME=string(min=1)
						BINARY=string(min=1)
						FAIL_LIMIT=integer(default=3, min=1)
						WARN_LIMIT=integer(default=0, min=0)
						RETRY_IMMEDIATELY=yes_no(default="Y")
						RETRY_WAIT_TIME=integer(default=0, min=0)
						TIMEOUT=integer(default=30, min=0)
						UT_SAMPLING=sample_option(default=list("SAMPLES: 3", "INTERVAL: 1"))
						UT_LIMIT=limit_option(default=list("WARN: 90", "ALERT: 98"))
						MEM_SAMPLING=sample_option(default=list("SAMPLES: 3", "INTERVAL: 1"))
						MEM_LIMIT=limit_option(default=list("WARN: 4000", "ALERT: 5000"))
						FD_LIMIT=limit_option(default=list("WARN: 3900", "ALERT: 4096"))
						FAIL_IF_MISSING=yes_no(default="Y")
						FAIL_IF_RESTARTED=yes_no(default="Y")
						MINIMUM_UPTIME=integer(default=120, min=0)
			[[[[CORE]]]]
				[[[[[SD]]]]]
					ENABLED=yes_no(default="N")
					NAME=string(default='sd', min=1)
					BINARY=string(default='sd', min=1)
					DIRS=force_string_list(default=list("/tmp"))
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					NAME_FORMAT=string(default="core*.*")
					CORE_LIMIT=limit_option(default=list("WARN: 1", "ALERT: 3"))
				[[[[[SSM]]]]]
					[[[[[[__many__]]]]]]
						NAME=string(min=1)
						ENABLED=yes_no(default="N")
						APPLICATION=string(min=1)
						BINARY=string(min=1)
						DIRS=force_string_list(default=list("/tmp"))
						FAIL_LIMIT=integer(default=3, min=1)
						WARN_LIMIT=integer(default=0, min=0)
						RETRY_IMMEDIATELY=yes_no(default="Y")
						RETRY_WAIT_TIME=integer(default=0, min=0)
						NAME_FORMAT=string(default="core*.*")
						CORE_LIMIT=limit_option(default=list("WARN: 1", "ALERT: 3"))
			[[[[DIR]]]]
				[[[[[__many__]]]]]
					NAME=string(min=1)
					DIR=string(min=1)
					ENABLED=yes_no(default="N")
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					DISK_SPACE_LIMIT=limit_option(default=list("WARN: 5000", "ALERT: 1000"))
					SIZE_LIMIT=limit_option(default=list("WARN: 45000", "ALERT: 50000"))
					TIMEOUT=integer(default=30, min=0)
			[[[[CUSTOM]]]]
				[[[[[__many__]]]]]
					NAME=string(min=1)
					ENABLED=yes_no(default="N")
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					TIMEOUT=integer(default=30, min=0)
					COMMAND=string(min=1)
					SUCCESS_EXIT_CODES=force_int_list(default=0)

	[[LSF]]
		CMD_TIMEOUT=integer(default=None, min=0)
		[[[CHECKS]]]
			[[[[RESPONSE]]]]
				[[[[[LIM]]]]]
					ENABLED=yes_no(default="N")
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					RESPONSE_LIMIT=limit_option(default=list("WARN: 30", "ALERT: 60"))
					TIMEOUT=integer(default=30, min=0)
				[[[[[MBATCHD]]]]]
					ENABLED=yes_no(default="N")
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					RESPONSE_LIMIT=limit_option(default=list("WARN: 30", "ALERT: 60"))
					TIMEOUT=integer(default=30, min=0)
					COMMAND=string(default="bsub -R 'selectt[]' hostname", min=1)
				[[[[[BLD]]]]]
					ENABLED=yes_no(default="N")
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					RESPONSE_LIMIT=limit_option(default=list("WARN: 30", "ALERT: 60"))
					TIMEOUT=integer(default=30, min=0)
				[[[[[BLCOLLECT]]]]]
					[[[[[[__many__]]]]]]
						ENABLED=yes_no(default="N")
						COLLECTOR_NAME=string(min=1, default=__default__)
						FAIL_LIMIT=integer(default=3, min=1)
						WARN_LIMIT=integer(default=0, min=0)
						RETRY_IMMEDIATELY=yes_no(default="Y")
						RETRY_WAIT_TIME=integer(default=0, min=0)
						TIMEOUT=integer(default=30, min=0)
			[[[[PERFORMANCE]]]]
				[[[[[SCHEDULER]]]]]
					ENABLED=yes_no(default="N")
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					TIMEOUT=integer(default=30, min=0)
					INTERVAL_SAMPLING=sample_option(default=list("SAMPLES: 4", "INTERVAL: 60"))
					INTERVAL_LIMIT=limit_option(default=list("WARN: 50", "ALERT: 60"))
			[[[[DAEMON]]]]
				[[[[[__many__]]]]]
					ENABLED=yes_no(default="N")
					NAME=string(min=1)
					BINARY=string(min=1)
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					TIMEOUT=integer(default=30, min=0)
					UT_SAMPLING=sample_option(default=list("SAMPLES: 3", "INTERVAL: 1"))
					UT_LIMIT=limit_option(default=list("WARN: 0", "ALERT: 0"))
					MEM_SAMPLING=sample_option(default=list("SAMPLES: 3", "INTERVAL: 1"))
					MEM_LIMIT=limit_option(default=list("WARN: 0", "ALERT: 0"))
					FD_LIMIT=limit_option(default=list("WARN: 0", "ALERT: 0"))
					FAIL_IF_MISSING=yes_no(default="Y")
					FAIL_IF_RESTARTED=yes_no(default="Y")
					MINIMUM_UPTIME=integer(default=120, min=0)
				[[[[[BLD]]]]]
					ENABLED=yes_no(default="N")
					NAME=string(min=1, default='bld')
					BINARY=string(min=1, default='bld')
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					TIMEOUT=integer(default=30, min=0)
					UT_SAMPLING=sample_option(default=list("SAMPLES: 3", "INTERVAL: 1"))
					UT_LIMIT=limit_option(default=list("WARN: 0", "ALERT: 0"))
					MEM_SAMPLING=sample_option(default=list("SAMPLES: 3", "INTERVAL: 1"))
					MEM_LIMIT=limit_option(default=list("WARN: 0", "ALERT: 0"))
					FD_LIMIT=limit_option(default=list("WARN: 0", "ALERT: 0"))
					FAIL_IF_MISSING=yes_no(default="Y")
					FAIL_IF_RESTARTED=yes_no(default="Y")
					MINIMUM_UPTIME=integer(default=120, min=0)
				[[[[[BLCOLLECT]]]]]
					[[[[[[__many__]]]]]]
						ENABLED=yes_no(default="N")
						NAME=string(min=1)
						BINARY=string(min=1, default='blcollect')
						COLLECTOR_NAME=string(min=1, default=__default__)
						FAIL_LIMIT=integer(default=3, min=1)
						WARN_LIMIT=integer(default=0, min=0)
						RETRY_IMMEDIATELY=yes_no(default="Y")
						RETRY_WAIT_TIME=integer(default=0, min=0)
						TIMEOUT=integer(default=30, min=0)
						UT_SAMPLING=sample_option(default=list("SAMPLES: 3", "INTERVAL: 1"))
						UT_LIMIT=limit_option(default=list("WARN: 0", "ALERT: 0"))
						MEM_SAMPLING=sample_option(default=list("SAMPLES: 3", "INTERVAL: 1"))
						MEM_LIMIT=limit_option(default=list("WARN: 0", "ALERT: 0"))
						FD_LIMIT=limit_option(default=list("WARN: 0", "ALERT: 0"))
						FAIL_IF_MISSING=yes_no(default="Y")
						FAIL_IF_RESTARTED=yes_no(default="Y")
						MINIMUM_UPTIME=integer(default=120, min=0)
			[[[[CORE]]]]
				[[[[[__many__]]]]]
					NAME=string(min=1)
					ENABLED=yes_no(default="N")
					BINARY=string(min=1)
					DIRS=force_string_list(default=list("/tmp"))
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					NAME_FORMAT=string(default="core*.*")
					CORE_LIMIT=limit_option(default=list("WARN: 1", "ALERT: 3"))
			[[[[DIR]]]]
				[[[[[__many__]]]]]
					ENABLED=yes_no(default="N")
					NAME=string(min=1)
					DIR=string(min=1)
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					DISK_SPACE_LIMIT=limit_option(default=list("WARN: 5000", "ALERT: 1000"))
					SIZE_LIMIT=limit_option(default=list("WARN: 45000", "ALERT: 50000"))
					TIMEOUT=integer(default=30, min=0)
			[[[[BLACKHOLE]]]]
				[[[[[__many__]]]]]
					ENABLED=yes_no(default="N")
					NAME=string(min=1)
					NAME_FORMAT=string(default="*")
					DIR=string(default='work/incoming')'
					FILE_ACTION=option(default='DELETE', 'MOVE', 'RENAME', 'DELETE')
					POST_PROCESSING=string(default="")
					MOVE_DIR=string(default='work/processed')
					RENAME_SUFFIX=string(default='.done')
					FAIL_SUFFIX=string(default='.failed')
					FAIL_LIMIT=integer(default=1, min=1, max=1)
					WARN_LIMIT=integer(default=0, min=0, max=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					DISABLE_ON_ALERT=yes_no(default="N")
			[[[[CUSTOM]]]]
				[[[[[__many__]]]]]
					NAME=string(min=1)
					ENABLED=yes_no(default="N")
					FAIL_LIMIT=integer(default=3, min=1)
					WARN_LIMIT=integer(default=0, min=0)
					RETRY_IMMEDIATELY=yes_no(default="Y")
					RETRY_WAIT_TIME=integer(default=0, min=0)
					TIMEOUT=integer(default=30, min=0)
					COMMAND=string(min=1)
					SUCCESS_EXIT_CODES=force_int_list(default=0)