import fresh_tomatoes
import media
bahubali = media.Movie("Bahubali",
                        "Baahubali: The Beginning, also known as BB1, is an Indian dramatic-action film directed by S. S. Rajamouli. The film was produced by Shobu Yarlagadda and Prasad Devineni and was shot in Telugu and Tamil",
                        "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwj-qL-ow9zYAhUGXbwKHTeRANEQjRwIBw&url=http%3A%2F%2Fwww.bollywoodhungama.com%2Fmovie%2Fbahubali-thebeginning%2Fcritic-review%2F&psig=AOvVaw3fEBu8tHzLfOcKsDDp6bVn&ust=1516193564069831",
                        "https://www.youtube.com/watch?v=sOEg_YZQsTI")
Airlift = media.Movie("Airlift",
                       "The film captures the story of the Indians stuck in Kuwait during that time, through the eyes of Ranjit Katiyal and a few other characters. This is a story about how these Indians, with the help of Ranjit Katiyal, managed to survive the Iraqi invasion, andagainst all odds, move across Iraq into Jordan, from where they were brought home to India by the largest ever Airlift attempted in the history of the world",
                       "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=imgres&cd=&cad=rja&uact=8&ved=0ahUKEwjYlK73ydzYAhUIyLwKHfcRC4cQjRwIBw&url=http%3A%2F%2Ft3.gstatic.com%2Fimages%3Fq%3Dtbn%3AANd9GcTHssC2lZ7sucnosiSRhwgT9_aZHwgr5wkEGWyX1Ov69cgAd8YS&psig=AOvVaw0uF75ckHQKTL16wNyosUfL&ust=1516195341240850",
                       "https://www.youtube.com/watch?v=vb5xCMbMfZ0")
Interstellar = media.Movie("Interstellar",
                            "In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand (Michael Caine), a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a wormhole. But first, Brand must send former NASA pilot Cooper (Matthew McConaughey) and a team of researchers through the wormhole and across the galaxy to find out which of three planets could be mankind's new home.",
                            "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=imgres&cd=&cad=rja&uact=8&ved=0ahUKEwjC7pKYy9zYAhUJwLwKHe6mCUcQjRwIBw&url=http%3A%2F%2Ft1.gstatic.com%2Fimages%3Fq%3Dtbn%3AANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB&psig=AOvVaw3G1R3_sdenembyQE-lFL8m&ust=1516195678543680",
                            "https://www.youtube.com/watch?v=2LqzF5WauAw")
Cook_Up = ("Cook Up a Storm",
          "A culinary competition becomes a battleground as a famous Cantonese street-food chef goes up against his Michelin-starred, classically trained rival.",
          "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=imgres&cd=&cad=rja&uact=8&ved=0ahUKEwj49vOo09zYAhWFvbwKHfW3CKoQjRwIBw&url=http%3A%2F%2Ft2.gstatic.com%2Fimages%3Fq%3Dtbn%3AANd9GcRokdzK9KRxQqaaHCoKr1eSbVnW8SGWfqVzHxgyVB_GZYNotPoo&psig=AOvVaw2a3ZfchlKk9_38ClqLCRHQ&ust=1516197861125576",
          "https://www.youtube.com/watch?v=CIcuh3Eiqgg")

movies = [bahubali, Airlift, Interstellar, Cook_Up]  
fresh_tomatoes.open_movies_page (movies)
                         