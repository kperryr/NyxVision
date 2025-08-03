package com.nyxvision.intelreporter.models;

import jakarta.persistence.*;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import org.hibernate.annotations.JdbcTypeCode;
import org.hibernate.type.SqlTypes;
import java.time.LocalDateTime;

import java.time.OffsetDateTime;
import java.util.List;
import java.util.Map;

@Entity
@Table(name = "intel_reports")
public class IntelReport {

    // No-arg constructor
    public IntelReport() {}

    @Id
    @Column(name = "reportId")
    private String reportId;

    private String region;

    @JdbcTypeCode(SqlTypes.JSON)
    @Column(columnDefinition = "jsonb")
    private List<Float> coordinates;

    @Column
    private OffsetDateTime timestamp;

    private String summary;
    private String classification;
    private  String source;

    @Column(name = "threatScore")
    private int threatScore;

    @JdbcTypeCode(SqlTypes.JSON)
    @Column(columnDefinition = "jsonb")
    private List<String> keywords;

    @Column(name = "fullText")
    private String fullText;

    @Column(name = "processedScore")
    private int processedScore;

    @JdbcTypeCode(SqlTypes.JSON)
    @Column(columnDefinition = "jsonb", name  = "processedKeywords")
    private Map<String, Integer> processedKeywords;

    @Column(name = "processedDate")
    private OffsetDateTime processedDate;

    //Getters

    public String getReportId() {
        return reportId;
    }

    public String getRegion() {
        return region;
    }

    public List<Float> getCoordinates() {
        return coordinates;
    }

    public OffsetDateTime getTimestamp() {
        return timestamp;
    }

    public String getSummary() {
        return summary;
    }

    public String getClassification() {
        return classification;
    }

    public String getSource() {
        return source;
    }

    public int getThreatScore() {
        return threatScore;
    }

    public List<String> getKeywords() {
        return keywords;
    }

    public String getFullText() {
        return fullText;
    }

    public int getProcessedScore() {
        return processedScore;
    }

    public Map<String, Integer> getProcessedKeywords() {
        return processedKeywords;
    }

    public OffsetDateTime getProcessedDate() {
        return processedDate;
    }
}
