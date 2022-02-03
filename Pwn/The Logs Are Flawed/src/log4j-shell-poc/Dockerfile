FROM tomcat:8.0.36-jre8

RUN rm -rf /usr/local/tomcat/webapps/*
ADD target/log4shell-1.0-SNAPSHOT.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080 
RUN echo "UiTHack22{There_Are_Bugs_In_The_LoGs}" > /flag.txt
RUN cp /flag.txt /usr/local/tomcat

RUN chmod -R 777 /usr/local/tomcat 
RUN useradd -u 5555 archive
USER archive

CMD ["catalina.sh", "run"]

