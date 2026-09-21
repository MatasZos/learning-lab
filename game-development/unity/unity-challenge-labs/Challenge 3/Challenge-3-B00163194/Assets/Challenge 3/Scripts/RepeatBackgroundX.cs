using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RepeatBackgroundX : MonoBehaviour
{
    private Vector3 startPos;
    private float repeatWidth;

    private void Start()
    {
        startPos = transform.position; // Establish the default starting position 
        // Set repeat width to half of the background's width (x-axis)
        repeatWidth = GetComponent<BoxCollider>().size.x / 2; 
    }

    private void Update()
    {
        // If background moves left by its repeat width, move it back to the start position
        if (transform.position.x < startPos.x - repeatWidth)
        {
            transform.position = startPos;
        }
    }
}
