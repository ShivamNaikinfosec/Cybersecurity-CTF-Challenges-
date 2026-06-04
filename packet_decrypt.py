from scapy.all import rdpcap, UDP

pcap_file = "traffic.pcap"

output_file = "flag.txt"

packets =rdpcap(pcap_file)
flags= []

for pkt in packets:
    if UDP in pkt:
        raw= bytes(pkt[UDP].payload)
        if raw:
            try:
               text = raw.decode("utf-8", errors="ignore")
               if  "{" in text and "}" in text:
                    if text not in  flags:
                        flags.append(text)
            except Exception:
                continue

if  flags:
     print(f"Found {len(flags)} flag(s): ")
     for  f in flags:
          print("   ",f)
     with  open(output_file, "w") as out:
        out.write("\n".join(flags)   + "/n")
     print(f"All flags saved to {output_file}")

else:
     print("No flags found in the capture")

