package com.nyxvision.intelreporter.models;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import java.time.LocalDateTime;
import java.util.HashMap;

@Entity
public class IntelReport {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    private String name;

    private double[] coordinates;

    private LocalDateTime timestamp;

    private String summary;

    private ENUM classification;

    private  String source;

    private int threatScore;

    private String[] keywords;

    private String fullText;

    private int processedScore;

    private HashMap<String, Integer> processedKeywords;

    private LocalDateTime processedDate;

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double[] getCoordinates() {
        return coordinates;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public String getSummary() {
        return summary;
    }

    public ENUM getClassification() {
        return classification;
    }

    public String getSource() {
        return source;
    }

    public int getThreatScore() {
        return threatScore;
    }

    public String[] getKeywords() {
        return keywords;
    }

    public String getFullText() {
        return fullText;
    }

    public int getProcessedScore() {
        return processedScore;
    }

    public HashMap<String, Integer> getProcessedKeywords() {
        return processedKeywords;
    }

    public LocalDateTime getProcessedDate() {
        return processedDate;
    }
}
