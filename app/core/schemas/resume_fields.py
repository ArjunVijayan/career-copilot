from __future__ import annotations
from pydantic import BaseModel


class ResumeFields(BaseModel):
    candidate_id: str | None = None
    name: str | None = None
    contact_info: ContactInfo | None = None
    education: list[Education] | None = None
    experience: list[Experience] | None = None
    skills: list[Skill] | None = None
    projects: list[Project] | None = None


class ContactInfo(BaseModel):
    location: str | None = None
    email: str | None = None
    phone: str | None = None
    linkedin: str | None = None
    github: str | None = None
    portfolio: str | None = None
    other_links: list[str] | None = None
    address: str | None = None

class Education(BaseModel):
    degree: str | None = None
    field_of_study: str | None = None
    institution: str | None = None
    location: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    description: str | None = None

class Experience(BaseModel):
    title: str | None = None
    company: str | None = None
    location: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    description: str | None = None
    skill_sets: list[str] | None = None

class Skill(BaseModel):
    name: str | None = None
    category: str | None = None
    proficiency: str | None = None

class Project(BaseModel):
    name: str | None = None
    description: str | None = None
    technologies: list[str] | None = None
    link: str | None = None

