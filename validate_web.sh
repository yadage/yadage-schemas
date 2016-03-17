#!/bin/sh
#publishers:
packtivity-validate testobjects/packtivity/publishers/constpub.yml -c from-github -n packtivity/publisher/constant-pub-schema

packtivity-validate testobjects/packtivity/publishers/constpub.yml -c from-github -n packtivity/publisher/constant-pub-schema
packtivity-validate testobjects/packtivity/publishers/globpub.yml -c from-github -n packtivity/publisher/fromglob-pub-schema
packtivity-validate testobjects/packtivity/publishers/parpub.yml -c from-github -n packtivity/publisher/frompar-pub-schema
packtivity-validate testobjects/packtivity/publishers/ymlpub.yml -c from-github -n packtivity/publisher/fromyaml-pub-schema

#environments:
packtivity-validate testobjects/packtivity/environments/dockerenv.yml -c from-github -n packtivity/environment/docker-enc-schema

#processes:
packtivity-validate testobjects/packtivity/processes/stringinterp.yml -c from-github -n packtivity/process/stringinterp-schema

#packtivities:
packtivity-validate testobjects/packtivity/packtivities/example_one.yml -c from-github -n packtivity/packtivity-schema

#schedulers:
packtivity-validate -s testobjects/yadage/schedulers single-from-ctx.yml -c from-github -n yadage/scheduler/single-from-ctx-schema
packtivity-validate -s testobjects/yadage/schedulers zip-from-dep.yml -c from-github -n yadage/scheduler/zip-from-dep-schema
packtivity-validate -s testobjects/yadage/schedulers reduce-from-dep.yml -c from-github -n yadage/scheduler/reduce-from-dep-schema
packtivity-validate -s testobjects/yadage/schedulers map-from-dep.yml -c from-github -n yadage/scheduler/map-from-dep-schema
packtivity-validate -s testobjects/yadage/schedulers map-from-ctx.yml -c from-github -n yadage/scheduler/map-from-ctx-schema

#stages:
packtivity-validate -s testobjects/yadage/stages stage_one.yml -c from-github -n yadage/stage-schema

#workflows:
packtivity-validate -s testobjects/yadage/workflows workflow_one.yml -c from-github -n yadage/workflow-schema

#utils:
packtivity-validate testobjects/utils/shallow.yml -c from-github -n utils/shallow-primitive-schema
