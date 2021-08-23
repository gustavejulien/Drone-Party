#include <gtkmm.h>
#include <iostream>
#include "PDCPApp.hpp"

int main (int argc, char **argv)
{
  auto app = Gtk::Application::create(argc, argv, "org.gtkmm.PDCPApp");
  PDCPApp *pdcpApp = new PDCPApp();
  app->run(*(pdcpApp->window));
  return 0;
}