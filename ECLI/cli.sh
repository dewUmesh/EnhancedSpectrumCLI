#!/bin/sh
CLIBASEDIR=`dirname $0`
java -cp $CLIBASEDIR/lib/spectrum-cli-runtime*.jar:$CLIBASEDIR/lib/* -Djava.util.logging.config.file=logging.properties com.pb.spectrum.cli.Bootstrap $*
