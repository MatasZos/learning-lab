using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class PlayerControllerX : MonoBehaviour
{
    public GameObject dogPrefab;
    private float coolDown = 1;
    // Update is called once per frame
    void Update()
    {
        // On spacebar press, send dog
        if (Input.GetKeyDown(KeyCode.Space) && coolDown <= 0)
        {
            coolDown = 1;
            Instantiate(dogPrefab, transform.position, dogPrefab.transform.rotation);
        }
        if (coolDown > -0)
        {
            coolDown -= Time.deltaTime;
        }

    }
}