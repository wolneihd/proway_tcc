package com.proway.backend.controllers;

import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.proway.backend.models.Frontend;

@RestController
@RequestMapping(value = "/frontend")
public class FrontendController {

    @GetMapping(produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Frontend> getInformation() {
        Frontend obj = new Frontend();
        return ResponseEntity.ok().body(obj);
    }

}
