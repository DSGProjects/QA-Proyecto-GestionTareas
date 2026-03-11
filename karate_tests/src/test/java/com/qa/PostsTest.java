package com.qa;

import com.intuit.karate.junit5.Karate;

class PostsTest {
    @Karate.Test
    Karate testPosts() {
        return Karate.run("posts").relativeTo(getClass());
    }
}