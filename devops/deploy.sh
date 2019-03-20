#!/usr/bin/env bash
ssh -o StrictHostKeyChecking=no root@47.47.47.47 << 'ENDSSH'
 cd /your_project_name
 docker login -u $REGISTRY_USER -p $CI_BUILD_TOKEN $CI_REGISTRY
 docker pull registry.gitlab.com/your_username/your_project_name:latest
 docker-compose up -d
ENDSSH
