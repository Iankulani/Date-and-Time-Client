# -*- coding: utf-8 -*-
"""
Created on Sun March  20 08:345:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Date and Time Client")
print(Fore.GREEN+font)

import socket

def start_client():
    # Prompt for the server's IP address and port
    server_host = input("Enter the server's IP address:")
    server_port = int(input("Enter the server's port number:"))
    
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect((server_host, server_port))
        
        # Receive the date and time from the server
        date_time = client_socket.recv(1024).decode()
        
        print(f"Received from server: {date_time}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_client()
