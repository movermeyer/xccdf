#!/bin/bash

echo "################################################################################"
echo "####                         CICLOMATIC COMPLEXITY                          ####"
echo "################################################################################"
echo ""

radon cc -s -a src/xccdf

echo "################################################################################"
echo "####                         MAINTAINABILITY INDEX                          ####"
echo "################################################################################"
echo ""

radon mi -s src/xccdf