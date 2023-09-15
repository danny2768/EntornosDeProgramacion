package com.example.ejemplo001;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SaludoControlador{
    @GetMapping(value = "saludo", produces = MediaType.TEXT_PLAIN_VALUE)
    public String saludo(){
        return "Bienvenidos al curso de Spring Boot";
    }
}