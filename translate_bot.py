#!/usr/bin/env python3
"""Telegram translation bot using DeepL API"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Telegram translation bot using DeepL API")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("translate-bot v0.1.0");return
 print(f"[12:01] translate-bot ready")
if __name__=="__main__":main()
