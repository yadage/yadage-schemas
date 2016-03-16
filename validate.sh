#!/bin/sh
#publishers:
packtivity-validate testobjects/packtivity/publishers/constpub.yml -c . -n schemas/packtivity/publisher/constant-pub-schema

packtivity-validate testobjects/packtivity/publishers/constpub.yml -c . -n schemas/packtivity/publisher/constant-pub-schema
packtivity-validate testobjects/packtivity/publishers/globpub.yml -c . -n schemas/packtivity/publisher/fromglob-pub-schema
packtivity-validate testobjects/packtivity/publishers/parpub.yml -c . -n schemas/packtivity/publisher/frompar-pub-schema
packtivity-validate testobjects/packtivity/publishers/ymlpub.yml -c . -n schemas/packtivity/publisher/fromyaml-pub-schema

#environments:
packtivity-validate testobjects/packtivity/environments/dockerenv.yml -c . -n schemas/packtivity/environment/docker-enc-schema

#processes:
packtivity-validate testobjects/packtivity/processes/stringinterp.yml -c . -n schemas/packtivity/process/stringinterp-schema

#packtivities:
packtivity-validate testobjects/packtivity/packtivities/example_one.yml -c . -n schemas/packtivity/packtivity-schema

#schedulers:
packtivity-validate -s testobjects/yadage/schedulers singlestep-from-ctx.yml -c . -n schemas/yadage/scheduler/single-from-ctx-schema
packtivity-validate -s testobjects/yadage/schedulers zip-from-dep.yml -c . -n schemas/yadage/scheduler/zip-from-dep-schema
packtivity-validate -s testobjects/yadage/schedulers reduce-from-dep.yml -c . -n schemas/yadage/scheduler/reduce-from-dep-schema
packtivity-validate -s testobjects/yadage/schedulers map-from-dep.yml -c . -n schemas/yadage/scheduler/map-from-dep-schema
packtivity-validate -s testobjects/yadage/schedulers map-from-ctx.yml -c . -n schemas/yadage/scheduler/map-from-ctx-schema

#stages:
packtivity-validate -s testobjects/yadage/stages stage_one.yml -c . -n schemas/yadage/stage-schema

#workflows:
packtivity-validate -s testobjects/yadage/workflows workflow_one.yml -c . -n schemas/yadage/workflow-schema

#utils:
packtivity-validate testobjects/utils/shallow.yml -c . -n schemas/utils/shallow-primitive-schema
