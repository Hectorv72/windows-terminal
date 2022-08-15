#!/bin/bash

FICHERO=$1

if [ -f $FICHERO ]
then
  echo true
else
  echo false
fi