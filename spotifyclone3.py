def spotify_options():

    while True:
        print("1. Access Song Options")
        print("2. Access Playlist Options")    # main spotify screen
        print("3. Access Queue Options")
        print("4. Quit Spotify")
        preference = input("Enter your choice: ")

        try: # check whether the input is valid
            preference = int(preference)
            assert 1 <= preference <= 4, "Your input is not within the range of 1 to 4" 
        except ValueError:
            print('Invalid Input')
        

        if preference == 1:
            print(manage_songs())
        elif preference == 2:
            print(manage_playlist())
        elif preference ==3: 
            print(manage_queue())
        elif preference == 4:
            print(quit_spotify())


class Queue:
        def __init__(self):
            self.queue = []
        def add_queue(self, song):
            self.queue.append(song)
            print(f"Added '{song}' to the queue.")
        def dequeue(self):
            if not self.queue_empty():
                return self.queue.pop(0)
        def queue_empty(self):
            return len(self.queue) == 0
        def show_queue(self):
            if self.queue_empty():
                print("Queue is empty.")
            else:
                print("The Queue Contents Are:")
                for song in self.queue:
                    print(song)
    
#Class with methods for adding, removing, and checking queue
queue = Queue()
def manage_queue():
        global queue
        while True:
            print("1. Add Songs to Queue?")
            print("2. Remove Songs from Queue?")
            print("3. Show Queue")
            print("4. Quit Queue Options")

            option = input("Enter your choice: ")

            try: # check whether the input is valid
                option = int(option)
                assert 1 <= option <= 4, "Your input is not within the range of 1 to 4" 
            except ValueError:
                print('Invalid Input')

            if option == 1:
                song = (input("What Songs Would you Like to Queue? (type 'done' to stop): "))
                if song == 'done' or song == 'Done':
                    break
                queue.add_queue(song)
#Prompts User What song they would like to add to the queue and adds it to the list through append
            if option == 2:
                dequeue = (input("Would you like to remove the first song from queue?(Y or N): "))
                if dequeue == 'Y' or 'y':
                    removed_song = queue.dequeue()
                    print(f"Removed '{removed_song}' from the queue.")
                else:
                    break
#Prompts User What song they would like to remove from the queue and removes it from the list through pop
            elif option == 3:
                queue.show_queue()
#Allows the User to see what the contents of the queue is
            elif option == 4:
                return "Quitting, one second"
#Allows the user to quit from the options of queue


    
playlist = {}
def manage_playlist():
        global playlist
        while True:
            print("1. Create a New Playlist")
            print("2. Add a Song to the Playlist?")
            print("3. Show a Playlist")
            print("4. Quit Playlist Options")

            command = input("Enter your choice: ")
            try: # check whether the input is valid
                command = int(command)
                assert 1 <= command <= 4, "Your input is not within the range of 1 to 4" 
            except ValueError:
                print('Invalid Input')
    #The prompt asks the user which route they would want to take into 4 options

            if command == 1:
                playlist_name = input("Enter the Name of the Playlist You Would Like to Make: ")
                playlist[playlist_name] = []
                print(f"Playlist '{playlist_name}' has been created.")
    #The first options asks them to create a playlist and to name it, making it it's own list

            elif command == 2:
                playlist_name = input("Enter the Name of the Playlist You Would Like to Access: ")
                if playlist_name in playlist:
                    song = input("Enter the name of the song: ")
                    playlist[playlist_name].append(song)
                else:
                    print(f"Error, '{playlist_name}' does not exist.")
    #The second option prompts the user to ask add a song to a playlist, asks them before what playlist they would want to access 

            elif command == 3:
                playlist_name = input("Enter the Name of the Playlist You Would Like to Access: ")
                if playlist_name in playlist:
                    if len(playlist[playlist_name]) == 0:
                        print("Playlist is empty.")
                    else:
                        print(f"Playlist {playlist_name}:")
                        for song in playlist[playlist_name]:
                            print(song) 
                else: 
                    print(f"Error, '{playlist_name}' does not exist.")
    #The third option is to show the user what is in a playlist and asks them what playlist they would like to access, if it is empty it would return that it is empty, otherwise it would simply print the songs from the list
            elif command == 4:
                return "Quiting, one second"
            else:
                print("Error, Please try again.")
    #To exit out of the options having to do with playlists option 4 is available

def manage_songs():
    while True:
        print("1. Play a Song?")
        print("2. Play a Song from Queue?")
        print("3. Play a Song from a Playlist?")
        print("4. Quit Song Options")

        answer = input("Enter your Choice:")
        try:
            answer = int(answer)
            assert 1 <= answer <= 4, "Your input is not within the range of 1 to 4"
        except ValueError:
            print('Invalid Input')

        if answer == 1:  # Play a song
            song_choice = input("What Song Would You Like To Play?: ")
            print("Playing:", song_choice)

        elif answer == 2:  # Play the first song in the queue and update it
            if queue.queue_empty():
                print("Queue is empty.")
            else:
                song_choice = queue.dequeue()
                print("Playing:", song_choice)

        elif answer == 3:  # Play a song from a desired playlist
            if not playlist:
                print("There are no playlists.")
            else:      #Gives the user to choose a playlist to access and asks for a song within the playlist to play
                playlist_name = input("Which playlist would you like to access?: ")
                if playlist_name in playlist:
                    playlist_songs = playlist[playlist_name]
                    if not playlist_songs:
                        print("Playlist is empty.")
                    else:
                        song_choice = input("Which song would you like to play?: ")
                        if song_choice in playlist_songs:
                            print("Playing:", song_choice)
                        else:
                            print("Song not found in the playlist.")
                else:
                    print("Playlist not found.")

        elif answer == 4:
            return "Quitting, one second"

        else:
            print("Error, please try again.")

def quit_spotify():
    return "Quitting Spotify, Have a great Day!"

spotify_options()
