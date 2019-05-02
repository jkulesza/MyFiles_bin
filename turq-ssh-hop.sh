#!/bin/bash

TURQ_REGEXP="^(sn|cj|ml|mu|pi|wf|ls|wc)-fe[1-9]?(\.lanl\.gov)?$"

if [[ $1 =~ $TURQ_REGEXP ]]; then
  exec ssh wtrw1.lanl.gov ssh "$@"
else
  exec ssh "$@"
fi
