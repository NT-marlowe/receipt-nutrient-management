import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ApiFetch = () => {
    const [posts, setPosts] = useState([]);

    // this function is to-be-implemented!!
    function postImages() {
        // axios.post('https://anysweb.co.jp/api/')
        // .then(res => console.log(res))
        console.log("Image has been posted");
    }

    // this function is to-be-implemented!!
    function getNutritionInfo() {
        // setPosts(res.data);
        axios.get('https://jsonplaceholder.typicode.com/posts')
        .then(res => {
            setPosts(res.data)
        });
    }
    
    useEffect(() => 
        {
            getNutritionInfo();
            postImages();
        }
        , []);
        
    // useEffect(() => {
    //     axios.get("http://localhost:8000/api/todo").then((res) => {
    //     setTodoList(res.data);
    //     });
    // }, [])
    //     -    
    
    return (
        <div>
            <ul>
                {
                    posts.map(post => 
                        <li key={post.id}>
                            {post.title}
                        </li>)
                }
            </ul>
        </div>
    );
}

export default ApiFetch