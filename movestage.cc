#include <unistd.h>
#include <ctype.h>
#include <sys/ioctl.h>
#include <errno.h>
#include <sstream>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string.h>
#include <stdlib.h>

#include "strlcpy.h"
#include <unistd.h>     // UNIX standard function definitions
#include <fcntl.h>      // File control definitions
#include <errno.h>      // Error number definitions
#include <termios.h>

using namespace std;

void movestage(mr) {

  int MR = mr;
  int USB;
  USB = open("/dev/ttyUSB0",O_RDWR | O_NOCTTY);

  struct termios tty;
  struct termios tty_old;
  memset (&tty, 0, sizeof tty);

  tty_old = tty;
  cfsetospeed (&tty, (speed_t)B9600);
  cfsetispeed (&tty, (speed_t)B9600);


  tty.c_cflag     &=  ~PARENB;            // Make 8n1
  tty.c_cflag     &=  ~CSTOPB;
  tty.c_cflag     &=  ~CSIZE;
  tty.c_cflag     |=  CS8;
  tty.c_cflag     &=  ~CRTSCTS;           // no flow control
  tty.c_cc[VMIN]   =  1;                  // read doesn't block
  tty.c_cc[VTIME]  =  5;                  // 0.5 seconds read timeout
  tty.c_cflag     |=  CREAD | CLOCAL;

  cfmakeraw(&tty);
  tcflush( USB, TCIFLUSH );

  string s = to_string(MR) + "\r";

  int sizeOf = s.size();
  int i = 0;
  int offset = 3;

  char cmd[100] = "MR ";

  while(i<sizeOf)
  {
     cmd[i+offset]=s[i];

     i++;
  }


  //cout << cmd << endl;
  int n_written = 0,
      spot = 0;

  do {
      n_written = write( USB, &cmd[spot], 1 );
      spot += n_written;
  } while (cmd[spot-1] != '\r' && n_written > 0);


  //string write_buffer = "MR "+ to_string(MR) + "\n";
  //cout << write_buffer <<endl;

  //write(USB,write_buffer.c_str(), (write_buffer.size() - 1));
  //printf("stage moved");
  close(USB);
}
