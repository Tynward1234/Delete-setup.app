bplist00�
X$versionY$archiverT$topX$objects ��_NSKeyedArchiver�	Troot��+1259=>CGKU$null�_attributedStringData]dataPersisterV$class����WNS.dataO�	import sys
import plistlib
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            sys.exit(1)
        return result.stdout
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

run_command(["idevicepair", "mode", "dfu"])
device = run_command(["idevicepair", "vet"]).strip()
run_command(["idevicepair", "pair", device])

run_command(["idevicediag", "mode", "recovery", device])

run_command(["ideviceenterrecovery", device])

domain = "com.apple.mobile.installation.plist"
bundle_id = "com.apple.mobile.mobileinstallation.poststaging"

plist = plistlib.readPlist("/private/var/mobile/Library/Caches/com.apple.mobile.installd.plist")
for app in plist["Bootstrap"]:
    if app["BundleIdentifier"] == bundle_id:
        result = run_command(["irecovery", "-n", "uninstall_application", bundle_id])
        if "Error" not in result:
            print(f"Successfully deleted {bundle_id}")
        else:
            print("Error: Failed to delete the app")

run_command(["ideviceenterrecovery", "exit", device])

run_command(["idevicepair", "unpair", device])
*(**(*
*(**(**(**(*S*(*f*(**(**(*�*(**(**(*�*(*	*(**(*H*(*���Z$classnameX$classes]NSMutableData�]NSMutableDataVNSDataXNSObject� !"#$%&'()*_accumulatedDataSize_objectIdentifierWallURLs_identifierToDataDictionary_cacheDirectoryURL �
�����,-./0WNS.base[NS.relative� ��_�file:///private/var/mobile/Containers/Data/Application/42F0B6FF-EF3F-401B-AD02-0F7BA88F96FC/tmp/pasteboardDataPersister/23EBAFE6-2EDF-42BC-8630-4B137EFEF40B�34UNSURL�3�678ZNS.objects��	�:;^NSMutableArray�:<WNSArray_$6FB23537-A8E4-43D0-B767-FFA8507AB5A1�?6@ABWNS.keys����DE_NSMutableDictionary�DF\NSDictionary�HI_ICDataPersister�J_ICDataPersister�LM_ICNotePasteboardData�N_ICNotePasteboardData    $ ) 2 7 I L Q S e k r � � � � � � � �������� 3FNk������������KPVY^ijlq��������������					#	:	=             O              	T