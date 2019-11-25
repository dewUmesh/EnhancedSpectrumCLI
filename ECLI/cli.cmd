@echo off
rem SET DEBUG_OPTS=-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5006

SET DEBUG_OPTS=
java %DEBUG_OPTS% -cp ../spectrumCLI_lib/lib/spectrum-cli-runtime*.jar;../spectrumCLI_lib/lib/* -Djava.util.logging.config.file=logging.properties -Dfile.encoding=UTF8 com.pb.spectrum.cli.Bootstrap %1 %2