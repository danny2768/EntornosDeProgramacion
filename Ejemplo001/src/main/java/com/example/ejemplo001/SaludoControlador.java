package com.example.ejemplo001;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SaludoControlador{
    @GetMapping(value = "saludo/{titulo}/{name}", produces = MediaType.TEXT_PLAIN_VALUE)
    public String saludo(@PathVariable("titulo") String t, @PathVariable("name") String n){
        return "Bienvenido " + t + " " + n + " al curso de Spring Boot";
    }
}