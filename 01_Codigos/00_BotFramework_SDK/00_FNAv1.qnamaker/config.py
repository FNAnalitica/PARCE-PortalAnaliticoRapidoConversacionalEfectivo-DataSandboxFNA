#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "")


    COSMOS_DB_URI=os.environ.get("CosmosDBUri", " ")
    COSMOS_DB_PRIMARY_KEY=os.environ.get("CosmosDBPrimaryKey"," ")
    COSMOS_DB_DATABASE_ID=os.environ.get("CosmosDBDataBaseID"," ")
    COSMOS_DB_CONTAINER_ID=os.environ.get("CosmosDBContainerID"," ")