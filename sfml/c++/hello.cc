 #include <SFML/Audio.hpp>
#include <iostream>
using namespace std;

 #include <SFML/Graphics.hpp>
 
 int main()
 {
     // Create the main window
     sf::RenderWindow App(sf::VideoMode(800, 600), "SFML window");
 
     // Load a sprite to display
     sf::Image my_image;

     if (!my_image.LoadFromFile("image.png"))
         return EXIT_FAILURE;

     sf::Sprite sprite(my_image);


 
     // Create a graphical string to display
     sf::Font Arial;
     sf::String Text("Hello SFML");
 
     // Load a music to play
     /*
     sf::Music Music;
     if (!Music.OpenFromFile("nice_music.ogg"))
         return EXIT_FAILURE;

     // Play the music
     Music.Play();
     */
 
     // Start the game loop
     while (App.IsOpened())
     {
         // Process events
         sf::Event Event;
         while (App.GetEvent(Event))
         {
             // Close window : exit
             if (Event.Type == sf::Event::Closed)
                 App.Close();
             
             if (Event.Type == sf::Event::MouseMoved)
                 ;

         if ((Event.Type == sf::Event::KeyPressed) && (Event.Key.Code == sf::Key::Escape))
            App.Close();


         }
 
         // Clear screen
         App.Clear();
 
         // Draw the sprite
         App.Draw(sprite);
 
         // Draw the string
         App.Draw(Text);
 
         // Update the window
         App.Display();
     }
 
     return EXIT_SUCCESS;
 }

