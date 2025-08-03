package com.nyxvision.intelreporter.controllers;

import com.nyxvision.intelreporter.models.IntelReport;
import com.nyxvision.intelreporter.repository.IntelReportRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/reports")
public class ListReportsController {

    @Autowired
    private IntelReportRepository intelReportRepository;

   @GetMapping
   public @ResponseBody Iterable<IntelReport> getAllReports(){
       return intelReportRepository.findAll();

   }
}
