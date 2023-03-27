
# WELCOME SCREEN
print("--------------------------------------------------")
print("              Capstone Project")
print("--------------------------------------------------")

print("\n")

true = 1
while (true):
 
  #  User inputs
  print("-------------Enter your information-------------")
  print("\n")
  referrer_url = input("Please enter referrer URL: ")
  host_IP = input("Please enter the host IP: ")
  user_IP = input("Please enter your IP address:")
  user_Location = input("What is your location: ")
  user_OS = input("Please enter your OS: ")
  user_Device = input("Please enter your device: ")
  
  print("\n")
  
  # -------------------------------------------------------------------------
  # Open a file for writing
  file = open("user_request.txt", "w")
  
  # Collect the information from the user and add to the file
  file.write("URL: " + referrer_url + "\n")
  file.write("Host IP: " + host_IP + "\n")
  file.write("User IP: " + user_IP + "\n")
  file.write("User Location: " + user_Location + "\n")
  file.write("User Operating System: " + user_OS + "\n")
  file.write("User Device: " + user_Device + "\n")
  # Close the file
  file.close()
  
  
  # -------------------------------------------------------------------------
  #  Declaring two lists - user_request_list & blocked_user_request_list to store
  valid_user_request_list = []
  blocked_user_request_list = []
  
  # -------------------------------------------------------------------------
  #  Checking the user input - Referrer URL
  
  if referrer_url == "www.allsafe.io/security/tunnel/POD:2208":
      print("Your referrer URL is valid!")
      valid_user_request_list.append(referrer_url)
  else:
      print("Your referrer URL is invalid!")
      blocked_user_request_list.append(referrer_url)
  print("\n")
  
  # -------------------------------------------------------------------------
  #  Checking the user input - User Location
  
  if user_Location == "Toronto":
      print("Your location is valid.")
      valid_user_request_list.append(user_Location)
  else:
      print("Your location is invalid.")
      blocked_user_request_list.append(user_Location)
  print("\n")
  
  # -------------------------------------------------------------------------
  #  Checking the user input - User Device
  
  if user_Device == "Desktop":
      print("Your device is valid.")
      valid_user_request_list.append(user_Device)
      
  else: 
      print("Your device is invalid.")
      blocked_user_request_list.append(user_Device)
  print("\n")
  
  # -------------------------------------------------------------------------
  #  Checking the user input - User OS
  
  if user_OS == 'Windows':
      print("Your operating system is valid.")
      valid_user_request_list.append(user_OS)
      
  else:
      print("Your operating system is invalid.")
      blocked_user_request_list.append(user_OS)
  
  print("\n")
  
  # -------------------------------------------------------------------------
  #  Checking the user input - User IP
  
  # Define the range of valid IP addresses
  min_IP = [234, 305, 0, 21]
  max_IP = [430, 640, 1, 63]
  
  # Check if the user's IP address is within the range
  def is_between(user_IP, min_IP, max_IP):
      user_IP_list = list(map(int, user_IP.split('.')))
      if all(min_IP[i] <= user_IP_list[i] <= max_IP[i] for i in range(4)):
          print("User IP address is: " + user_IP + ". In range.")
          valid_user_request_list.append(user_IP)
          return True
      else:
          print("User IP address is: " + user_IP + ". Out of range.")
          blocked_user_request_list.append(user_IP)
          return False
  
  # Call the function to check if the user's IP address is within the range
  is_between(user_IP, min_IP, max_IP)
  print("\n")
  
  # -------------------------------------------------------------------------
  #  Checking the user input - Host IP
  
  # Define the range of valid IP addresses
  min_Host_IP = [10, 0, 24, 123]
  max_Host_IP = [12, 1, 23, 164]
  
  # Check if the user's IP address is within the range
  def is_between(host_IP, min_Host_IP, max_Host_IP):
      user_IP_list = list(map(int, user_IP.split('.')))
      if all(min_IP[i] <= user_IP_list[i] <= max_IP[i] for i in range(4)):
          print("Host IP address is: " + host_IP + ". In range.")
          valid_user_request_list.append(host_IP)
          return True
      else:
          print("Host IP address is: " + host_IP + ". Out of range.")
          blocked_user_request_list.append(host_IP)
          return False
  
  # Call the function to check if the user's IP address is within the range
  is_between(host_IP, min_Host_IP, max_Host_IP)
  print("\n")
  
  # ----------------------------------------------------------------
  #  Determine whether the user request is valid ot not
  
  print("valid_user_request_list", valid_user_request_list)
  print("\n")
  size = len(valid_user_request_list)
  # print('User Request list size:', size)
  print("\n")
  if size >= 3:
    print('User Request is valid!')
    print("\n")
  else:
    print('User Request is Invalid/Malicious!')
    print("\n")
    print("Blocked_user_request_list", blocked_user_request_list)
    print("\n")
   
    # View blocked request
    user_request = open("user_request.txt", 'r')
    print("Blocked user request text file[OPEN] " + "user_request.txt" )
    print("\n")
    print("------------------Blocked User Request----------------------" )
    for line in user_request:
      print(line) # View Blocked Request- Display the user request file contents
  
    # Open a file for writing the blocked request
    file = open("blocked_user_requests.txt", "a")
    
    # Collect the information from the blocked user request and add to the file
    
    file.write("URL: " + referrer_url + "\n")
    file.write("Host IP: " + host_IP + "\n")
    file.write("User IP: " + user_IP + "\n")
    file.write("User Location: " + user_Location + "\n")
    file.write("User Operating System: " + user_OS + "\n")
    file.write("User Device: " + user_Device + "\n")
    file.write("---------------------------------\n")
    # Close the file
    file.close()
  
  print("----------------------END----------------------------")
  print("\n")
  continue