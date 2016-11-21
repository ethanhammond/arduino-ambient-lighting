CC := g++

#The Target Binary Program
TARGET := average-color

#The Directories, Source, Includes, Objects, Binary and Resources
SRCDIR := src
INCDIR := include
BUILDDIR := obj
TARGETDIR := bin
# Uncomment if there are files in resources
# TODO: make sure this works
# RESDIR := res
SRCEXT := cpp
DEPEXT := d
OBJEXT := o

#Flags, Libraries and Includes
CFLAGS := -O3 -fPIC -g -Wall -Werror
LIB := -L/usr/lib
INC := -I$(INCDIR) -I/usr/include
INCDEP := -I$(INCDIR)

#Uncomment to send the binary somewhere over the rainbow
# DISTPATH = root@192.168.7.2:~/phoebe-2.0/

#---------------------------------------------------------------------------------
#DO  NOT  EDIT  BELOW  THIS LINE
#THIS IS WHERE THE MAGIC HAPPENS
#---------------------------------------------------------------------------------
SOURCES := $(shell find $(SRCDIR) -type f -name *.$(SRCEXT))
OBJECTS := $(patsubst $(SRCDIR)/%,$(BUILDDIR)/%,$(SOURCES:.$(SRCEXT)=.$(OBJEXT)))

#Default Make
all: resources $(TARGET) copy

#Remake
remake: cleaner all

#Copy Resources from Resources Directory to Target Directory
resources: directories
ifdef RESDIR
	@rsync -r $(RESDIR)/* $(TARGETDIR)/
endif

#Make the Directories
directories:
	@mkdir -p $(TARGETDIR)
	@mkdir -p $(BUILDDIR)

#Clean only Objects
clean:
	@$(RM) -rf $(BUILDDIR)

#Full Clean, Objects and Binaries
cleaner: clean
	@$(RM) -rf $(TARGETDIR)

#Copy file to external source
copy:
ifdef DISTPATH
	scp -r $(TARGETDIR)/* $(DISTPATH)
endif

#Pull in dependency info for *existing* .o files
-include $(OBJECTS:.$(OBJEXT)=.$(DEPEXT))

#Link
$(TARGET): $(OBJECTS)
	$(CC) -o $(TARGETDIR)/$(TARGET) $^ $(LIB)

#Compile
$(BUILDDIR)/%.$(OBJEXT): $(SRCDIR)/%.$(SRCEXT)
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<
	@$(CC) $(CFLAGS) $(INCDEP) -MM $(SRCDIR)/$*.$(SRCEXT) > $(BUILDDIR)/$*.$(DEPEXT)
	@cp -f $(BUILDDIR)/$*.$(DEPEXT) $(BUILDDIR)/$*.$(DEPEXT).tmp
	@sed -e 's|.*:|$(BUILDDIR)/$*.$(OBJEXT):|' < $(BUILDDIR)/$*.$(DEPEXT).tmp > $(BUILDDIR)/$*.$(DEPEXT)
	@sed -e 's/.*://' -e 's/\\$$//' < $(BUILDDIR)/$*.$(DEPEXT).tmp | fmt -1 | sed -e 's/^ *//' -e 's/$$/:/' >> $(BUILDDIR)/$*.$(DEPEXT)
	@rm -f $(BUILDDIR)/$*.$(DEPEXT).tmp

#Non-File Targets
.PHONY: all remake clean cleaner resources
