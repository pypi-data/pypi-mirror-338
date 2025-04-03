#!/usr/bin/env python3
import os
import sys
import time
from rich.console import Console

console = Console()

def clear_screen():
    # Clear the terminal screen using rich's built-in clear method
    console.clear()

def full_justify_paragraph(paragraph, width):
    """
    Given a paragraph string and desired width, return a list of fully justified lines.
    This algorithm groups words into lines such that the total length (including spaces)
    equals the width.
    """
    words = paragraph.split()
    lines = []
    i = 0
    while i < len(words):
        j = i
        line_length = 0
        # Determine how many words can fit into the line
        while j < len(words) and line_length + len(words[j]) + (j - i) <= width:
            line_length += len(words[j])
            j += 1
        num_words = j - i
        # For the last line or a line with one word, left-justify
        if j == len(words) or num_words == 1:
            line = " ".join(words[i:j])
            line = line.ljust(width)
        else:
            total_spaces = width - line_length
            space_between = total_spaces // (num_words - 1)
            extra_spaces = total_spaces % (num_words - 1)
            line = ""
            for k in range(i, j - 1):
                # Distribute extra spaces among the leftmost gaps
                spaces = space_between + (1 if (k - i) < extra_spaces else 0)
                line += words[k] + " " * spaces
            line += words[j - 1]
        lines.append(line)
        i = j
    return lines

def typewriter_print(text, style="white", delay=0.001, justify=True):
    """
    Print the given text using a typewriter effect.
    If justify is True, the text is first split into paragraphs and each paragraph is fully justified
    to the console width.
    """
    # When justification is enabled, use the current console width.
    width = console.width if justify else None
    # Split text into paragraphs (double-newlines separate paragraphs)
    paragraphs = text.split("\n")
    for para in paragraphs:
        # Remove any newlines within the paragraph
        para = para.replace("\n", " ")
        if justify and width:
            lines = full_justify_paragraph(para, width)
        else:
            # If not justifying, simply split the text at newlines.
            lines = para.splitlines() if para else [""]
        for line in lines:
            for char in line:
                # Print each character with the given style and a small delay.
                console.print(char, style=style, end="")
                sys.stdout.flush()
                time.sleep(delay)
            console.print("")  # Newline after each line
        console.print("")  # Extra newline between paragraphs

def main():
    clear_screen()

    # Header Section
    console.rule("Rahul Raj")
    header = (
        "Kochi, Kerala, India | +91 9930532257\n"
        "Email: rahulrajpl@gmail.com\n"
        "Website: https://randomwalk.in/ | LinkedIn: https://www.linkedin.com/in/rahulrajpl/"
    )
    typewriter_print(header, style="cyan")

    # Professional Profile
    console.rule("Professional Profile")
    # typewriter_print("Professional Profile", style="magenta", delay=0.01, justify=False)
    profile = (
        "Seasoned military leader with 14 years of diverse expertise in leading teams and executing high-stakes missions. "
        "Proficient in leveraging advanced IT technologies, including Artificial Intelligence (AI), Machine Learning (ML), "
        "and Cybersecurity, to optimize operational efficiency and maintain information superiority. Possess a proven track record "
        "in implementing security regulations, streamlining processes, executing projects, and spearheading training and development initiatives. "
        "Dedicated to excellence and committed to safeguarding digital assets while advancing technological capabilities."
    )
    typewriter_print(profile, style="white")
    
    # Core Competencies
    console.rule("Core Competencies")
    # typewriter_print("Core Competencies", style="magenta", delay=0.01, justify=False)
    competencies = [
        "Leadership/ Strategy",
        "Team Management",
        "Project Management",
        "Artificial Intelligence/ Machine Learning",
        "Cybersecurity, Governance, Risk and Compliance",
        "IT enabled Services and IT Life Cycle Management",
    ]
    for comp in competencies:
        typewriter_print(f"• {comp}", style="yellow")

    # Experience Section
    # typewriter_print("Experience", style="magenta", delay=0.01, justify=False)
    console.rule("Experience")

    # Head of Department (Technical)
    typewriter_print("Head of Department (Technical) (Mar 2023 – Present)", style="green", delay=0.01, justify=False)
    hod_points = [
        "Led the warship’s Technical Department with innovation through in-house projects, ensuring efficient power generation despite resource constraints and outdated systems. Strengthened IT services and enhanced cybersecurity by identifying operational risks and applying effective mitigation strategies, demonstrating strong leadership and problem-solving in a challenging maritime environment."
    ]
    for point in hod_points:
        typewriter_print(f"  • {point}", style="white")

    # Chief Instructor & Staff Officer (IT)
    typewriter_print("Chief Instructor & Staff Officer (IT) (Aug 2020 – Feb 2023)", style="green", delay=0.01, justify=False)
    ci_points = [
        "Trained over 2,000 Navy personnel in IT, Security, and Embedded Systems. Organized national AI and Data Science workshops for tri-services. Developed an AI-based Predictive Maintenance Module for warships. Delivered 50+ lectures on AI/ML, decision-making with Excel, Linux, and cybersecurity, promoting tech adoption and operational efficiency."]
    for point in ci_points:
        typewriter_print(f"  • {point}", style="white")

    # Deputy Director
    typewriter_print("Deputy Director (May 2015 – Jul 2018)", style="green", delay=0.01, justify=False)
    dd_points = [
        "Managed IT infrastructure and services for 1,500+ users over 11,000+ acres at Naval Base Karwar. Secured confidential digital and physical assets, executed a facility management contract to address resource gaps, and led ₹200+ crore IT projects, including setting up a disaster recovery site to boost digital resilience."]
    for point in dd_points:
        typewriter_print(f"  • {point}", style="white")

    # Assistant Director
    typewriter_print("Assistant Director (Oct 2013 – Apr 2015)", style="green", delay=0.01, justify=False)
    ad_points = [
        "Maintained electrical equipment for optimal performance and managed IT assets throughout their lifecycle for efficient use. Developed and deployed a Remote Monitoring and Reporting Tool onboard a warship, enabling real-time machinery status tracking, which improved operational efficiency and optimized manpower utilization."]
    for point in ad_points:
        typewriter_print(f"  • {point}", style="white")

    # Certifications Section
    # typewriter_print("Certifications", style="magenta", delay=0.01, justify=False)
    console.rule("Courses/ Upskilling")
    certifications = [
        "AI Product Management, Duke University (via Coursera)",
        "AI Agents Fundamentals, HuggingFace.co",
        "Business Statistics and Analysis, Rice University (via Coursera)",
        "Machine Learning for Cybersecurity, CDAC Hyderabad",
        "Cybersecurity Policy, Indian Institute of Technology, Delhi",
        "Cybersecurity for Business Specialization, University of Colorado (via Coursera)",
        "Introduction to Cybersecurity Tools & Cyber Attacks, IBM",
        "Introduction to Autopsy Digital Forensics Platform, BasisTech",
        "Deep Learning Specialization, DeepLearning.AI",
        "TensorFlow in Practice Specialization, DeepLearning.AI",
        "Fundamentals of Open-Source Management, Linux Foundation",
        "Blockchain for Managers, Commonwealth of Learning"
    ]
    for cert in certifications:
        typewriter_print(f"• {cert}", style="yellow")

    # Education Section
    # typewriter_print("Education", style="magenta", delay=0.01, justify=False)
    console.rule("Education")
    education = [
        "Certificate Programme in International Business Management (2024) - Indian Institute of Management, Indore, MP, India",
        "Master of Technology in Computer Science and Engineering (2020) - Indian Institute of Technology Kanpur, UP, India",
        "Bachelor of Technology in Computer Science and Engineering (2010) - Cochin University of Science and Technology, Kerala, India"
    ]
    for edu in education:
        typewriter_print(f"• {edu}", style="cyan")

if __name__ == '__main__':
    main()
