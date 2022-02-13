#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
__copyright__ = ('Copyright Amazon.com, Inc. or its affiliates. '
                 'All Rights Reserved.')
__version__ = '2.6.1-beta.3'
__license__ = 'MIT-0'
__author__ = 'Akihiro Nakajima'
__url__ = 'https://github.com/aws-samples/siem-on-amazon-opensearch-service'

from aws_cdk import core

from deployment_samples.deployment_samples_stack import (
    ADLogExporterStack,
    CoreLogExporterStack,
    CWLNoCompressExporterStack,
    DeploymentSamplesStack,
    EventBridgeEventsExporterStack,
    FirehoseExporterStack,
    WorkSpacesLogExporterStack,
)

app = core.App()
DeploymentSamplesStack(app, "DeploymentSamplesStack")
basic_logging = CoreLogExporterStack(
    app, "siem-log-exporter-core",
    description=(f'SIEM on Amazon OpenSearch Service v{__version__}: '
                 'log exporter - core resource'))
cwl_nocompresss_logging = CWLNoCompressExporterStack(
    app, "siem-log-exporter-cwl-nocompress",
    description=(f'SIEM on Amazon OpenSearch Service v{__version__}: '
                 'log exporter - CWL resource without compress'))
fsx_logging = FirehoseExporterStack(
    app, "siem-log-exporter-fsx",
    description=(f'SIEM on Amazon OpenSearch Service v{__version__}: '
                 'log exporter - FSx resource without compress'),
    default_firehose_name='aws-fsx-',
    firehose_compression_format='GZIP')
workspaces_logging = WorkSpacesLogExporterStack(
    app, "siem-log-exporter-workspaces",
    description=(f'SIEM on Amazon OpenSearch Service v{__version__}: '
                 'log exporter - Workspaces'))
ad_logging = ADLogExporterStack(
    app, "siem-log-exporter-ad",
    description=(f'SIEM on Amazon OpenSearch Service v{__version__}: '
                 'log exporter - Active Directory'))
eventbridge_events_logging = EventBridgeEventsExporterStack(
    app, "siem-log-exporter-eventbridge-events",
    description=(f'SIEM on Amazon OpenSearch Service v{__version__}: '
                 'log exporter - EventBridge events '
                 '(SecurityHub, ConfigRules)'))

app.synth()
