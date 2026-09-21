using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpawnManagerX : MonoBehaviour
{
    public GameObject[] objectPrefabs; // Array of prefabs to spawn
    private float spawnDelay = 2; // Delay before the first spawn
    private float spawnInterval = 1.5f; // Time interval between spawns

    private PlayerControllerX playerControllerScript; // Reference to the player controller

    // Start is called before the first frame update
    void Start()
    {
        // Correctly invoke the SpawnObjects method instead of PrawnsObject
        InvokeRepeating("SpawnObjects", spawnDelay, spawnInterval);
        playerControllerScript = GameObject.Find("Player").GetComponent<PlayerControllerX>();
    }

    // Method to spawn objects
    void SpawnObjects()
    {
        // Set random spawn location and random object index
        Vector3 spawnLocation = new Vector3(30, Random.Range(5, 15), 0);
        int index = Random.Range(0, objectPrefabs.Length);

        // If game is still active, spawn new object
        if (!playerControllerScript.gameOver)
        {
            Instantiate(objectPrefabs[index], spawnLocation, objectPrefabs[index].transform.rotation);
        }
    }
}
