import wmi

# raw_wql = "SELECT * FROM __InstanceCreationEvent WITHIN 2 WHERE TargetInstance ISA \'Win32_USBHub\'"
raw_wql = "SELECT * FROM __InstanceCreationEvent " + "WITHIN 2 " + "WHERE TargetInstance ISA 'Win32_PnPEntity'"
c = wmi.WMI()
watcher = c.watch_for(raw_wql=raw_wql)
while 1:
    usb = watcher()
    print(usb)


# instance of Win32_PnPEntity
# {
#         Caption = "JetFlash Transcend 16GB USB Device";
#         ClassGuid = "{4d36e967-e325-11ce-bfc1-08002be10318}";
#         CompatibleID = {"USBSTOR\\Disk", "USBSTOR\\RAW", "GenDisk"};
#         ConfigManagerErrorCode = 0;
#         ConfigManagerUserConfig = FALSE;
#         CreationClassName = "Win32_PnPEntity";
#         Description = "Disk drive";
#         DeviceID = "USBSTOR\\DISK&VEN_JETFLASH&PROD_TRANSCEND_16GB&REV_1100\\17QQQD7NDTRJ40ST&0";
#         HardwareID = {"USBSTOR\\DiskJetFlashTranscend_16GB__1100", "USBSTOR\\DiskJetFlashTranscend_16GB__", "USBSTOR\\DiskJetFlash", "USBSTOR\\JetFlashTranscend_16GB__1", "JetFlashTranscend_16GB__1", "USBSTOR\\GenDisk", "GenDisk"};
#         Manufacturer = "(Standard disk drives)";
#         Name = "JetFlash Transcend 16GB USB Device";
#         PNPClass = "DiskDrive";
#         PNPDeviceID = "USBSTOR\\DISK&VEN_JETFLASH&PROD_TRANSCEND_16GB&REV_1100\\17QQQD7NDTRJ40ST&0";
#         Present = TRUE;
#         Service = "disk";
#         Status = "OK";
#         SystemCreationClassName = "Win32_ComputerSystem";
#         SystemName = "DESKTOP-KCNTGCB";
# };
