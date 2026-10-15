#!/usr/bin/env python3
"""
Module Name: advanced_forensic_extractor.py
Description: Multi-protocol streaming packet parser with an active Base64 extraction layer.
Author: Shivam Naik
"""

import sys
import os
import base64
import re
from scapy.all import PcapReader, TCP, UDP

# Standard CTF flag identifier regex pattern (matches flag{...} style structures)
FLAG_REGEX = re.compile(r"[a-zA-Z0-9_\-]+{[^}]+}")

def attempt_base64_decode(raw_string: str) -> str:
    """
    Scans a plaintext string for Base64 blocks and evaluates them for valid decodes.
    """
    # Regex to hunt for potential Base64 strings (multiples of 4 characters)
    b64_pattern = re.compile(r'(?:[A-Za-z0-9+/]{4}){2,}(?:==| South Africa|=)?')
    matches = b64_pattern.findall(raw_string)
    
    decrypted_fragments = []
    for match in matches:
        try:
            decoded_bytes = base64.b64decode(match)
            decoded_text = decoded_bytes.decode('utf-8', errors='ignore')
            if any(char in decoded_text for char in ["{", "}", "_"]):
                decrypted_fragments.append(decoded_text)
        except Exception:
            continue
    return " ".join(decrypted_fragments)

def analyze_traffic(pcap_path: str, output_path: str) -> None:
    """
    Streams multi-protocol frames to extract plaintext and obfuscated flags dynamically.
    """
    if not os.path.exists(pcap_path):
        sys.stderr.write(f"[!] Error: Target file '{pcap_path}' not found.\n")
        sys.exit(1)

    print(f"[*] Initializing deep forensic sequence for: {pcap_path}")
    flags = set()
    packet_count = 0

    try:
        with PcapReader(pcap_path) as packet_stream:
            for pkt in packet_stream:
                packet_count += 1
                payload_bytes = b""

                # Isolate transport layer payload strings
                if pkt.haslayer(TCP):
                    payload_bytes = bytes(pkt[TCP].payload)
                elif pkt.haslayer(UDP):
                    payload_bytes = bytes(pkt[UDP].payload)

                if not payload_bytes:
                    continue

                # Safely convert bytes to working string
                decoded_payload = payload_bytes.decode("utf-8", errors="ignore")

                # Track plain text matches vs potential encoded variants
                search_space = decoded_payload + " " + attempt_base64_decode(decoded_payload)
                
                # Check for standard flag signatures using regex
                found_flags = FLAG_REGEX.findall(search_space)
                for flag in found_flags:
                    clean_flag = flag.strip()
                    if clean_flag not in flags:
                        flags.add(clean_flag)
                        print(f"[+] Extracted flag structure: {clean_flag}")

        print(f"[*] Post-analysis update: Scanned {packet_count} total packets.")

        if flags:
            print(f"[+] Total distinct flags found: {len(flags)}. Exporting files...")
            with open(output_path, "w", encoding="utf-8") as out:
                out.write("\n".join(flags) + "\n")
            print(f"[+] Evidence file successfully built at: {output_path}")
        else:
            print("[-] Forensic scan yielded zero flag patterns inside this capture.")

    except KeyboardInterrupt:
        sys.stderr.write("\n[!] Analysis sequence aborted by user.\n")
        sys.exit(130)

if __name__ == "__main__":
    TARGET_PCAP = "traffic.pcap"
    EXTRACTED_DATA = "flag.txt"
    
    analyze_traffic(TARGET_PCAP, EXTRACTED_DATA)
